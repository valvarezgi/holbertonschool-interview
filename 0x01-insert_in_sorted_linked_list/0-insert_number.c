#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Start of the linked list.
 * @number: Number to insert into the list.
 * Return: Address of the new node, or NULL if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *tmp = *head, *new;

    new = malloc(sizeof(listint_t));
    if (!new)
        return (NULL);
    new->n = number;
    if (!*head)
    {
        *head = new;
        new->next = NULL;
	return (new);
    }
    if (tmp->n > number)
    {
        new->next = tmp;
        *head = new;
        return (new);
    }
    while (tmp->next)
    {
        if (tmp->next->n > number)
        {
            new->next = tmp->next;
            tmp->next = new;
            break;
        }
        tmp = tmp->next;
    }
    if (!tmp->next)
        tmp->next = new;
    return (new);
}
