#include "wiringPi.h"

char LED=15;

int main(void){
    
    if(wiringPiSetup() < 0) return -1;
    pinMode (LED,OUTPUT);
    
    while(1){

        digitalWrite(LED,0);
        LED=15; // reg light
        digitalWrite(LED,1);
        delay(200);
        
        digitalWrite(LED,0);
        LED=16; // green light
        digitalWrite(LED,1);
        delay(200);
        
        digitalWrite(LED,0);
        LED=1; // blue light
        digitalWrite(LED,1);
        delay(200);
        
        // dark
        digitalWrite(LED,0);
        delay(200);
    }
}