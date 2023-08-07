#include "lists.h"

/**
 * check_cycle - Check if a singly linked list has a cycle using
 * the "Tortoise and Hare" algorithm.
 * @list: Pointer to the head of the linked list.
 *
 * Return: 1 if a cycle is detected, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	if (list == NULL || list->next == NULL)
		return (0);

	tortoise = list;
	hare = list->next;

	while (tortoise && hare && hare->next)
	{
		if (tortoise == hare)
			return (1);

		tortoise = tortoise->next;
		hare = hare->next->next;
	}

	return (0);
}
