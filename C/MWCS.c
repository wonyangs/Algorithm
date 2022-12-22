#include <stdio.h>
#include <stdlib.h>

// t_graph - graph infomation struct
// matrix : graph infomation matrix (edge and weight)
// size : vertices count
typedef struct s_graph
{
	int **matrix;
	int size;
}	t_graph;

// t_node - clique set
// vertice_list : vertice numbers that make up clique
// size : size of vertice_list
// total_weight : total weight of clique
typedef struct s_node
{
	int				*vertice_list;
	int				size;
	int				total_weight;
	struct s_node	*next;
}	t_node;

// t_list - List ADT
typedef struct s_list
{
	t_node	*head;
	int		size;
}	t_list;


/*
	List control functions
*/
// Initialize node with information of clique
t_node	*init_node(int size)
{
	t_node	*node;

	node = (t_node *)malloc(sizeof(t_node));
	node->vertice_list = (int *)malloc(sizeof(int) * size);
	node->total_weight = 0;
	node->size = size;
	node->next = NULL;
	return (node);
}

// Initialize List ADT
t_list	*init_list(void)
{
	t_list	*list;

	list = (t_list *)malloc(sizeof(t_list));
	list->head = init_node(0);
	list->size = 0;
	return (list);
}

// Used in lst_addback function
// Check that both nodes have the same content
// cand->vertice_list are always sorted
static int	is_same_cand(t_node *cand1, t_node *cand2)
{
	for (int i = 0; i < cand1->size; i++)
	{
		if (cand1->vertice_list[i] != cand2->vertice_list[i])
			return (0);
	}
	return (1);
}

// List ADT method
// Add a node to list
// If there is the same content in the list, this work is ignored
void	lst_addback(t_list *list, t_node *node)
{
	t_node	*now;

	now = list->head;
	while (now->next)
	{
		// check that nodes such as nodes to add are in the list
		if (is_same_cand(now->next, node))
			return ;
		now = now->next;
	}
	// if there is no same node, add a node to list.
	now->next = node;
	list->size += 1;
}


// Deallocates matrix
void	free_matrix(int **matrix, int size)
{
	for (int i = 0; i < size; i++)
		free(matrix[i]);
	free(matrix);
}

// Initialize a matrix with size (N + 1) * (N + 1)
// And receive input of edge infomation
// If here is an error, this function return a NULL pointer
int	**init_matrix(int N, int M)
{
	int	a, b, w;
	int	**matrix;

	// allocate matrix
	matrix = (int **)malloc(sizeof(int *) * (N + 1));
	if (!matrix)
		return (NULL);
	for (int i = 0; i < N + 1; i++)
	{
		matrix[i] = (int *)malloc(sizeof(int) * (N + 1));
		if (!(matrix[i]))
		{
			free_matrix(matrix, i);
			return (NULL);
		}
		// initialize each cell by 0
		for (int j = 0; j < N + 1; j++)
			matrix[i][j] = 0;
	}

	// receive input of edge infomation
	for (int i = 0; i < M; i++)
	{
		scanf("%d %d %d", &a, &b, &w);
		if (a == b || a <= 0 || a > N || b <= 0 || b > N || w < 1)
			continue ;
		// update matrix
		matrix[a][b] = w;
		matrix[b][a] = w;
	}
	return (matrix);
}

// Initialize first clique list
// In this function, clique have only two element
t_list	*init_cand_list(t_graph graph)
{
	t_list	*cand_list = init_list();
	t_node	*cand;

	for (int i = 0; i < graph.size + 1; i++)
	{
		for (int j = i; j < graph.size + 1; j++)
		{
			// add minimum clique
			if (graph.matrix[i][j] != 0)
			{
				cand = init_node(2);
				cand->vertice_list[0] = i;
				cand->vertice_list[1] = j;
				cand->total_weight = graph.matrix[i][j];
				lst_addback(cand_list, cand);
			}
		}
	}
	return (cand_list);
}

// Deallocates List ADT
void	free_cand_list(t_list *cand_list)
{
	t_node	*node;
	t_node	*nxt_node;

	node = cand_list->head;
	nxt_node = cand_list->head->next;
	while (nxt_node)
	{
		free(node->vertice_list);
		free(node);
		node = nxt_node;
		nxt_node = node->next;
	}
	free(node->vertice_list);
	free(node);
	free(cand_list);
}

// Used in update_cand_list function
// Check vertice n to add to new clique. if vertice n can't be new clique, it returns -1
// If vertice n can be new clique, return new clique's weight
static int	calculate_new_weight(t_graph graph, t_node *cand, int n)
{
	int	weight = 0;
	int	vertice_num;

	for (int i = 0; i < cand->size; i++)
	{
		vertice_num = cand->vertice_list[i];
		// vertice n can't be new clique
		if (graph.matrix[vertice_num][n] == 0)
			return (-1);
		weight += graph.matrix[vertice_num][n];
	}
	return (weight);
}

// Used in update_cand_list function
// Create new clique node
// The new clique is an extension of n from the existing clique
// Return new clique node
static t_node	*copy_cand(t_node *cand, int n, int new_weight)
{
	t_node	*new_cand;
	int		tmp;

	// copy existing clique
	new_cand = init_node(cand->size + 1);
	new_cand->total_weight = cand->total_weight + new_weight;
	for (int i = 0; i < cand->size; i++)
		new_cand->vertice_list[i] = cand->vertice_list[i];
	// extend new vertice n
	new_cand->vertice_list[cand->size] = n;
	// sorting vertice_list to make same array
	for (int i = 0; i < cand->size + 1; i++)
	{
		for (int j = i + 1; j < cand->size + 1; j++)
		{
			if (new_cand->vertice_list[i] > new_cand->vertice_list[j])
			{
				tmp = new_cand->vertice_list[i];
				new_cand->vertice_list[i] = new_cand->vertice_list[j];
				new_cand->vertice_list[j] = tmp;
			}
		}
	}
	return (new_cand);
}

// Update clique list
// Each clique extend new vertice
t_list	*update_cand_list(t_graph graph, t_list *cand_list)
{
	t_list	*new_cand_list = init_list();
	t_node	*cand, *new_cand;
	int		new_weight;

	cand = cand_list->head->next;
	while (cand)
	{
		for (int i = 1; i < graph.size + 1; i++)
		{
			// calculate new clique's weight
			new_weight = calculate_new_weight(graph, cand, i);
			if (new_weight == -1)
				continue ;
			// make new clique node and add to new clique list
			new_cand = copy_cand(cand, i, new_weight);
			lst_addback(new_cand_list, new_cand);
		}
		cand = cand->next;
	}
	// deallocate existing clique list
	free_cand_list(cand_list);
	return (new_cand_list);
}

// Update maximum clique
void	update_maximal_cand(t_node **max_cand, t_list *cand_list)
{
	t_node	*new_cand;
	t_node	*cand;

	new_cand = NULL;
	cand = cand_list->head->next;
	// search clique list
	while (cand)
	{
		// if find clique bigger then existing maximum clique,
		// update maximum clique
		if ((*max_cand)->total_weight < cand->total_weight)
		{
			new_cand = init_node(cand->size);
			new_cand->total_weight = cand->total_weight;
			for (int i = 0; i < cand->size; i++)
				new_cand->vertice_list[i] = cand->vertice_list[i];
			free((*max_cand)->vertice_list);
			free((*max_cand)); 
			*max_cand = new_cand;
		}
		cand = cand->next;
	}
}

// Maximum Weight Clique Search
int	main(void)		
{
	int		N, M;
	t_graph	graph;
	t_list	*cand_list;
	t_node	*maximal;

	// Receive input of vertice count N and edge count M
	scanf("%d %d", &N, &M);

	// Initialize a matrix which containing graph information
	graph.size = N;
	graph.matrix = init_matrix(N, M);
	if (!graph.matrix)
		return (1);
	
	// Initialize maximum clique
	maximal = init_node(1);

	// Initialize clique list and update maximum clique
	cand_list = init_cand_list(graph);
	update_maximal_cand(&maximal, cand_list);
	
	// Loop until no new clique are found
	while (cand_list->size != 0)
	{
		cand_list = update_cand_list(graph, cand_list);
		update_maximal_cand(&maximal, cand_list);
	}

	// Print maximum weight clique
	printf("maximum weight clique : ");
	for (int i = 0; i < maximal->size; i++)
		printf("%d ", maximal->vertice_list[i]);
	printf("\nweight : %d\n", maximal->total_weight);

	// Deallocate part
	free_matrix(graph.matrix, graph.size);
	free_cand_list(cand_list);
	free(maximal->vertice_list);
	free(maximal);
	return (0);
}
