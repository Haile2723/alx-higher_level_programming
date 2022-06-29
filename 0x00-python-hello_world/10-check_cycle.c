/*
 * File: 10-check_cycle.c
 * Auth: Haile2723
 */

#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list contain a cycle.
 * @list: A singly linked list
 * Return: If there is a cycle - 1, O/W - 0.
 */

int check_cycle(listint_t *list)
{
listint_t *dog, *cat;

if (list == NULL || list->next == NULL)
return (0);

dog = list->next;
cat = list->next->next;

while (dog && cat && cat->next)
{
if (dog == cat)
return (1);

dog = dog->next;
cat = cat->next->next;
}

return (0);
}
