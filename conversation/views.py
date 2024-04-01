from django.shortcuts import get_object_or_404, redirect, render
from item.models import Item
from .models import Conversation, ConcernMessage
from .forms import ConversationMessageForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json


@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect("dashboard:index")

    conversations = Conversation.objects.filter(item=item).filter(
        members__in=[request.user.id]
    )

    if conversations:
        return redirect("conversation:detail", pk=conversations.first().id)

    if request.method == "POST":
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect("item:detail", pk=item_pk)

    else:
        form = ConversationMessageForm()

    return render(request, "conversation/new.html", {"form": form})


@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    return render(request, "conversation/inbox.html", {"conversations": conversations})


@login_required
def detail(request, pk):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == "POST":
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect("conversation:detail", pk=pk)

    else:
        form = ConversationMessageForm()

    return render(
        request,
        "conversation/detail.html",
        {"conversation": conversation, "form": form},
    )


@login_required
def concern_messages(request):
    messages = ConcernMessage.objects.all()

    return render(request, "conversation/concern.html", {"messages": messages})


@login_required
def concern_action(request, email):
    print(f"Email sent: {email}.")
    return redirect("conversation:concern")


@login_required
def delete_concern_message(request, pk):
    message = get_object_or_404(ConcernMessage, pk=pk)
    message.delete()

    return redirect("conversation:concern")


@require_POST
def submit_action(request, email):
    data = json.loads(request.body)
    action_data = data.get("action_data")

    print(action_data)

    # Process the action_data as needed (save to the database, etc.)

    return JsonResponse({"message": "Action received successfully"})
