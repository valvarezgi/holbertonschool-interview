#include "lists.h"



/**
 * reverse_first_half - reverses first half of the singly linked list
 * @head: pointer to pointer to head of list
 * @len: length of list
 * @i: incrementer
 * Return: pointer to last node in list
 */

listint_t *reverse_first_half(listint_t **head, int len, int i)
{
	listint_t *after, *current;

	current = *head;
	if (i < len / 2 - 1 && (*head)->next)
	{
		*head = (*head)->next;
		after = reverse_first_half(head, len, i + 1);
		after->next = current;
		return (current);
	}
	return (current);
}

/**
 * is_palindrome - determines if singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head, *first, *back = *head, *p;
	int len = 0, i = 0;

	if (!head || !(*head) || !(*head)->next)
		return (1);

	while (current)
	{
		current = current->next;
		len++;
	}

	for (i = 0; i < len / 2 - 1; ++i)
		back = back->next;

	if (len % 2 == 0)
		back = back->next;
	else
	{
		back = back->next;
		back = back->next;
	}

	p = reverse_first_half(head, len, 0);
	p->next = NULL;

	first = *head;

	while (back)
	{
		if (first->n != back->n)
			return (0);
		first = first->next;
		back = back->next;
	}

	return (1);
}