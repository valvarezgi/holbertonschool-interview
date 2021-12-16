#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Start of the linked list.
 * @number: Number to insert into the list.
 * Return: Address of the new node, or NULL if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = NULL;
	listint_t *aux = NULL;



	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;

	if (*head == NULL)
	{
		*head = node;
		node->next = NULL;
		return (node);
	}
	aux = *(head);
	if (aux->n >= number)
	{
		node->next = aux;
		*(head) = node;
		return (node);
	}

	while (aux->next != NULL)
	{
		if (aux->next->n > number)
		{
			node->next = aux->next;
			aux->next = node;
			return (node);
		}
		aux = aux->next;
	}
	aux->next = node;
	node->next = NULL;
	return (node);
}
