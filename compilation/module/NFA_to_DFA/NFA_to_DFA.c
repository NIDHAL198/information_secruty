#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STATES 100
#define MAX_SYMBOLS 10

typedef struct
{
   int transitions[MAX_STATES][MAX_SYMBOLS];
   int num_states;
   int num_symbols;
} NFA;

typedef struct
{
   int transitions[MAX_STATES][MAX_SYMBOLS];
   int num_states;
   int num_symbols;
} DFA;

void convertNFAtoDFA(NFA *nfa, DFA *dfa)
{
   int state_set[MAX_STATES][MAX_STATES] = {{0}};
   int dfa_states[MAX_STATES][MAX_STATES] = {{0}};
   int dfa_state_count = 0;

   int initial_set[MAX_STATES] = {1}; 
   memcpy(dfa_states[dfa_state_count++], initial_set, sizeof(initial_set));

   dfa->num_symbols = nfa->num_symbols;

   for (int i = 0; i < dfa_state_count; i++)
   {
      for (int symbol = 0; symbol < nfa->num_symbols; symbol++)
      {
         int new_set[MAX_STATES] = {0};

         for (int state = 0; state < nfa->num_states; state++)
         {
            if (dfa_states[i][state])
            {
               for (int target = 0; target < nfa->num_states; target++)
               {
                  if (nfa->transitions[state][symbol] == target)
                  {
                     new_set[target] = 1;
                  }
               }
            }
         }

         int found = 0;
         for (int j = 0; j < dfa_state_count; j++)
         {
            if (memcmp(dfa_states[j], new_set, sizeof(new_set)) == 0)
            {
               found = 1;
               dfa->transitions[i][symbol] = j;
               break;
            }
         }

         if (!found)
         {
            memcpy(dfa_states[dfa_state_count], new_set, sizeof(new_set));
            dfa->transitions[i][symbol] = dfa_state_count++;
         }
      }
   }

   dfa->num_states = dfa_state_count;
}

void printDFA(DFA *dfa)
{
   printf("DFA Transitions:\n");
   for (int i = 0; i < dfa->num_states; i++)
   {
      for (int j = 0; j < dfa->num_symbols; j++)
      {
         printf("DFA State %d, Symbol %d -> DFA State %d\n", i, j, dfa->transitions[i][j]);
      }
   }
}

int main()
{
   NFA nfa;
   nfa.num_states = 3;
   nfa.num_symbols = 2;

   memset(nfa.transitions, -1, sizeof(nfa.transitions));
   nfa.transitions[0][0] = 1;
   nfa.transitions[0][1] = 0;
   nfa.transitions[1][0] = 2;
   nfa.transitions[1][1] = 1;

   DFA dfa;
   convertNFAtoDFA(&nfa, &dfa);
   printDFA(&dfa);

   return 0;
}
