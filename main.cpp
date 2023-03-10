//Title:          EmergencyOverride
//Description:    Emergency override for E-vessel controls (demo box)
//Author:         Lassi Lahti
//Using analog sticks, should work with handles acting as potentiometers

//Jos teet Arduino IDE:llä, poista tämä
////////////////////////
#include <Arduino.h>////
////////////////////////

//Remote
#define VRY1 A0

//Local
#define VRY2 A1
#define override_btn 9
#define override_led 8

//Motor?
//#define motorPin 7

//Switch for modes
#define swPin1 3
#define swPin2 4
#define swPin3 5

//Misc

//Mapping vriables
int local_map;
int remote_map;

//Zero position check for local and remote
int remZero;
int locZero;

//Remote and local input reading
int remIn;
int locIn;

//Button for transfering control/emergency override
int btnState;
int emgBtnState;

//variable for checking mode, starts with local control
int recieve = 0;

//Mode switch and states for switching demo box modes
int sw = 1;
int swState1;
int swState2;
int swState3;

//Should start with local control
void setup() {


  //Serial
  Serial.begin(9600);
  Serial.println("BEGINNING LOCAL");

  //Override
  pinMode(override_btn, INPUT);
  pinMode(override_led, OUTPUT);

  //Switch pins
  pinMode(swPin1, INPUT);
  pinMode(swPin2, INPUT);
  pinMode(swPin3, INPUT);

}

//reset to remote control with local control at point 0, button pushed
void mode1(){

  //DEBUG/INFO//
  //Remote 257 --> 250 - 260
  //Local 245 --> 240 - 250
  //Serial.println(remote_map);
  //Serial.println(local_map);

  if(recieve == 0){
    digitalWrite(override_led, HIGH);
  }else{
    digitalWrite(override_led, LOW);
  }
  
  btnState = digitalRead(override_btn);

  //Incoming
  remIn = analogRead(VRY1);
  locIn = analogRead(VRY2);

  //Mapping joysticks
  remote_map = map(remIn, 0, 1024, 0, 512);
  local_map = map(locIn, 0,1024, 0, 512);

  //Local zero
  if ((local_map < 250) && (local_map > 240)){
    locZero = 1;
  }else{
    locZero = 0;
    recieve = 0;
  }
  //Remote con
  if((locZero == 1) && (recieve == 1)){
    Serial.print("REMOTE: ");
    Serial.println(remote_map);
    delay(500);
  }else if((recieve == 0)){
    Serial.print("OVERRIDE, LOCAL: ");
    Serial.println(local_map);
    delay(500);
  }

  if ((locZero == 1) && (btnState == HIGH)){
    recieve = 1;
  }
}

//TBD, Tähän koodi moodille jossa lisätty erillinen hätäseis (sama kuin 1 moodi, lisää tarkistus onko hätäseis painettu)
void mode2(){


}

//TBD, Tähän koodi mahdolliselle kolmannelle vaihtoehdolle
void mode3(){


}


void loop() {

  //Switch states
  swState1 = digitalRead(swPin1);
  swState2 = digitalRead(swPin2);
  swState3 = digitalRead(swPin3);

  //Mode 1
  while(swState1 == HIGH){
    mode1();
  }

  //Mode 2
  while(swState2 == HIGH){

    Serial.print("TBD");
    delay(300);
    Serial.print("Go away");
    delay(300);

  }

  //Mode 3
  while(swState3 == HIGH){

    Serial.print("TBD");
    delay(300);
    Serial.print("Go away");
    delay(300);

  }

}