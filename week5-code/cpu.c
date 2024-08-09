#include <stdio.h>

int main() {
    // Declare variables
    FILE *temperatureFile;
    int temperature;
    
    // Open the file that contains the CPU temperature
    temperatureFile = fopen("/sys/class/thermal/thermal_zone0/temp", "r");
    
    // Check if the file was opened successfully
    if (temperatureFile == NULL) {
        printf("Failed to open temperature file\n");
        return 1;
    }
    
    // Read the temperature from the file
    fscanf(temperatureFile, "%d", &temperature);
    
    // Close the file
    fclose(temperatureFile);
    
    // Convert temperature to degrees Celsius
    temperature = temperature / 1000;
    
    // Print the temperature
    printf("CPU Temperature: %d°C\n", temperature);
    
    return 0;
}
