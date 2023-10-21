# Import necessary modules and functions
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import ToDoItem, ToDoList

# Define a ListView for displaying a list of ToDoLists
class ListListView(ListView):
    model = ToDoList  # Specify the model to use (ToDoList)
    template_name = "todo_app/index.html"  # Template for rendering the list of ToDoLists

# Define another ListView for displaying a list of ToDoItems for a specific ToDoList
class ItemListView(ListView):
    model = ToDoItem  # Specify the model to use (ToDoItem)
    template_name = "todo_app/todo_list.html"  # Template for rendering the list of ToDoItems

    def get_queryset(self):
        # Customize the queryset to filter ToDoItems by the specified ToDoList (from URL parameter)
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        # Customize the context data to include the specific ToDoList
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context

# Define a CreateView for creating new ToDoLists
class ListCreate(CreateView):
    model = ToDoList  # Specify the model to use (ToDoList)
    fields = ["title"]  # Fields to include in the form for creating a ToDoList

    def get_context_data(self):
        # Customize the context data to include a title for the creation page
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Add a new list"
        return context

# Define a CreateView for creating new ToDoItems for a specific ToDoList
class ItemCreate(CreateView):
    model = ToDoItem  # Specify the model to use (ToDoItem)
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
    ]  # Fields to include in the form for creating a ToDoItem

    def get_initial(self):
        # Customize initial data by including the specified ToDoList (from URL parameter)
        initial_data = super(ItemCreate, self).get_initial()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        initial_data["todo_list"] = todo_list
        return initial_data

    def get_context_data(self):
        # Customize the context data to include the specific ToDoList and a title for the creation page
        context = super(ItemCreate, self).get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        context["todo_list"] = todo_list
        context["title"] = "Create a new item"
        return context

    def get_success_url(self):
        # Specify the URL to redirect to after successfully creating a ToDoItem
        return reverse("list", args=[self.object.todo_list_id])

# Define an UpdateView for updating existing ToDoItems
class ItemUpdate(UpdateView):
    model = ToDoItem  # Specify the model to use (ToDoItem)
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
    ]  # Fields to include in the form for updating a ToDoItem

    def get_context_data(self):
        # Customize the context data to include the specific ToDoList and a title for the update page
        context = super(ItemUpdate, self).get_context_data()
        context["todo_list"] = self.object.todo_list
        context["title"] = "Edit item"
        return context

    def get_success_url(self):
        # Specify the URL to redirect to after successfully updating a ToDoItem
        return reverse("list", args=[self.object.todo_list_id])

# Define a DeleteView for deleting ToDoLists
class ListDelete(DeleteView):
    model = ToDoList  # Specify the model to use (ToDoList)

    success_url = reverse_lazy("index")  # Specify the URL to redirect to after deleting a ToDoList
    # Use reverse_lazy() to avoid URL loading issues (e.g., circular imports)

# Define a DeleteView for deleting ToDoItems
class ItemDelete(DeleteView):
    model = ToDoItem  # Specify the model to use (ToDoItem)

    def get_success_url(self):
        # Specify the URL to redirect to after successfully deleting a ToDoItem
        return reverse_lazy("list", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs):
        # Customize the context data to include the specific ToDoList
        context = super().get_context_data(**kwargs)
        context["todo_list"] = self.object.todo_list
        return context
