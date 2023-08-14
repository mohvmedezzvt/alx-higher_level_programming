#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 0 if not a palindrome, 1 if a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow, *mid, *second_half, *next_node;
	listint_t *current1, *current2;
	int is_palindrome = 1;

	slow = *head;
	fast = *head;
	mid = NULL;
	prev_slow = NULL;

	/* finds the middle of the linked list */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next; /* moves twice as fast as the slow */
		prev_slow = slow; /* is the node before the middle */
		slow = slow->next; /* when fast reaches the end slow is in the middle */
	}

	/* If the list has an odd number of elements */
	if (fast != NULL)
	{
		mid = slow; /* assign the middle node to mid */
		slow = slow->next; /* slow moved to the next node */
	}

	/* Reverses the second half of the list */
	second_half = slow; /* slow points to the beginning of the second half */
	prev_slow->next = NULL; /* disconnecting the first have from the second half*/
	while (second_half != NULL)
	{
		next_node = second_half->next; /* store the next node in the original order*/
		second_half->next = mid; /* The next pointer of the current node\
		is updated to point to the mid node */
		mid = second_half; /* The mid pointer is moved to point to the current node*/
		second_half = next_node; /* The second_half pointer
		is moved to the next node in the original order */
	}

	current1 = *head;
	current2 = mid; /* current2 pointer starts from the new head of the reversed second half */
	/* compares the elements of the first half and the reversed second half of the linked list */
	while (current1 != NULL && current2 != NULL)
	{
		if (current1->n != current2->n)
		{
			is_palindrome = 0;
			break;
		}
		current1 = current1->next; /* The current1 pointer is moved to the next node in the first half */
		current2 = current2->next; /* The current2 pointer is moved to the next node in the reversed second half */
	}

	second_half = mid; /* the head of the reversed second half of the linked list */
	mid = prev_slow; /* the last node of the first half of the linked list */
	/* itrates through the reversed second half to reverses it back to its original order */
	while (second_half != NULL)
	{
		next_node = second_half->next; /* to store the next node in the original order of the reversed second half */
		second_half->next = mid; /* The next pointer of the current node in the reversed second half is set to point to the previous node (mid) */
		mid = second_half; /* mid pointer is updated to point to the current node */
		second_half = next_node; /* second_half pointer is moved to the next node in the original order of the reversed second half */
	}
	/* connecting the two halves back together in their original order */
	prev_slow->next = mid; /* the next pointer of the last node of the first half (prev_slow) is set to point to the new head of the reversed second half (mid) */

	return (is_palindrome);
}
