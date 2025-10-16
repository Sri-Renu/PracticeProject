#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void speak(const char *text) {
    char command[300] = "espeak \"";
    strcat(command, text);
    strcat(command, "\"");
    system(command);
}

int main() {
    char input[200];

    printf("👋 Welcome to the Text-to-Speech program!\n");
    printf("Type something and it will be spoken aloud.\n");
    printf("Type exit to quit.\n\n");

    while (1) {
        printf("Enter text: ");
        fgets(input, sizeof(input), stdin);

        // Remove newline
        input[strcspn(input, "\n")] = 0;

        if (strcmp(input, "exit") == 0) {
            printf("Goodbye! 👋\n");
            speak("Goodbye!");
            break;
        }

        if (strlen(input) == 0) {
            printf("⚠️ You entered nothing. Try again.\n");
            speak("You entered nothing. Try again.");
            continue;
        }

        // Speak the text
        speak(input);
        printf("✅ Spoken: %s\n\n", input);
    }

    return 0;
}
