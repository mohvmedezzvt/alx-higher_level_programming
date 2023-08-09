#include "lists.h"

/**
 * insert_node - Inserts a new node into a sorted linked list
 * @head: Pointer to a pointer to the head of the linked list
 * @number: The value to be inserted into the linked list
 *
 * Return: Address of the newly inserted node, or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *previous;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	current = *head;
	previous = NULL;

	while (current && current->n < number)
	{
		previous = current;
		current = current->next;
	}

	if (previous == NULL)
	{
		new->next = *head;
		*head = new;
	} else
	{
		previous->next = new;
		new->next = current;
	}

	return (new);
}
