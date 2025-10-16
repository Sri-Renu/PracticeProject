#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h> // For checking file existence

int main() {
    char input[200];

    printf("👋 Hello! Welcome to the file opener program.\n");
    printf("Type commands like: start filename.txt\n");
    printf("Type exit to quit the program.\n\n");

    while (1) {
        printf("Enter command: ");
        fgets(input, sizeof(input), stdin);

        // Remove newline
        input[strcspn(input, "\n")] = 0;

        // Exit check
        if (strcmp(input, "exit") == 0) {
            printf("Goodbye! 👋\n");
            break;
        }

        // Check if command starts with "start "
        if (strncmp(input, "start ", 6) == 0) {
            char *filename = input + 6; // skip "start "

            if (strlen(filename) == 0) {
                printf("⚠️ Error: No filename provided.\n");
            } else {
                // Check if file exists
                if (GetFileAttributes(filename) == INVALID_FILE_ATTRIBUTES) {
                    printf("⚠️ Error: File '%s' does not exist.\n", filename);
                } else {
                    char command[220] = "start ";
                    strcat(command, filename);
                    system(command);
                    printf("✅ File '%s' should now be open.\n", filename);
                }
            }
        } else {
            printf("⚠️ Invalid command. Use: start filename.txt or exit\n");
        }
    }

    return 0;
}