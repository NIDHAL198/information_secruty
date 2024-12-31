#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STATES 100
#define MAX_SYMBOLS 10

typedef struct
{
   int transitions[MAX_STATES][MAX_SYMBOLS];        
   int epsilon_transitions[MAX_STATES][MAX_STATES]; 
   int num_states;                                  
   int num_symbols;                                 
} NFA;

void initializeNFA(NFA *nfa, int num_states, int num_symbols)
{
   nfa->num_states = num_states;
   nfa->num_symbols = num_symbols;
   for (int i = 0; i < num_states; i++)
   {
      for (int j = 0; j < num_symbols; j++)
      {
         nfa->transitions[i][j] = -1; 
      }
      for (int k = 0; k < num_states; k++)
      {
         nfa->epsilon_transitions[i][k] = 0; 
      }
   }
}

void addEpsilonTransition(NFA *nfa, int from, int to)
{
   nfa->epsilon_transitions[from][to] = 1;
}

void epsilonClosure(NFA *nfa, int state, int closure[MAX_STATES], int visited[MAX_STATES])
{
   if (visited[state])
      return; 
   visited[state] = 1;
   closure[state] = 1;
   for (int i = 0; i < nfa->num_states; i++)
   {
      if (nfa->epsilon_transitions[state][i])
      {
         epsilonClosure(nfa, i, closure, visited); 
      }
   }
}

void removeEpsilonTransitions(NFA *nfa)
{
   for (int state = 0; state < nfa->num_states; state++)
   {
      int closure[MAX_STATES] = {0};
      int visited[MAX_STATES] = {0};
      epsilonClosure(nfa, state, closure, visited);
      for (int i = 0; i < nfa->num_states; i++)
      {
         if (closure[i])
         {
            for (int symbol = 0; symbol < nfa->num_symbols; symbol++)
            {
               if (nfa->transitions[i][symbol] != -1)
               {
                  nfa->transitions[state][symbol] = nfa->transitions[i][symbol];
               }
            }
         }
      }
   }
}

void printNFA(NFA *nfa)
{
   printf("Transitions:\n");
   for (int i = 0; i < nfa->num_states; i++)
   {
      for (int j = 0; j < nfa->num_symbols; j++)
      {
         if (nfa->transitions[i][j] != -1)
         {
            printf("State %d -> Symbol %d -> State %d\n", i, j, nfa->transitions[i][j]);
         }
      }
   }
}

int main()
{
   NFA nfa;
   initializeNFA(&nfa, 3, 2); 
   addEpsilonTransition(&nfa, 0, 1);
   addEpsilonTransition(&nfa, 1, 2);
   // printNFA(&nfa);
   nfa.transitions[2][0] = 2; 
   printf("after removing\t\t");
   printNFA(&nfa);
   removeEpsilonTransitions(&nfa);
   printNFA(&nfa);
   return 0;
}
