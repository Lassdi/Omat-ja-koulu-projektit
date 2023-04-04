//Title:          EmergencyOverride
//Description:    Emergency override for E-vessel controls (demo box)
//Author:         Lassi Lahti
//Using analog sticks, should work with handles acting as potentiometers

//Jos teet Arduino IDE:llä, poista tämä
////////////////////////
//#include <Arduino.h>////
////////////////////////

//Remote
#define VRY1 A0

//Local
#define VRY2 A1
#define override_btn 9
#define override_led 8
#define emgBtn 7
#define modeBtn 10
#define emgLed 11

//Motor?
//#define motorPin 7

//Switch for modes
#define swPin1 3
#define swPin2 4
#define swPin3 5

//Misc

//Mode switch message
bool printedModeChangeMsg = false;

//Mapping vriables
int local_map;
int remote_map;

//Zero position check for local and remote
int remZero;
int locZero;

//Remote and local input reading
int remIn;
int locIn;

//Buttons for transfering control and emergency override
int btnState;
int emgBtnState;
int lastState = 1;
int emgState = 1;


//variable for checking mode, starts with local control
int recieve;

//Mode switch and states for switching demo box modes
int modeState;
int lastMode = HIGH;
int currentMode = 1;

//Should start with local control
void setup() {


  //Serial
  Serial.begin(9600);
  Serial.println("BEGINNING LOCAL");

  //Override
  pinMode(override_btn, INPUT);
  pinMode(override_led, OUTPUT);
  pinMode(emgLed, OUTPUT);

  //Mode switch
  pinMode(modeBtn, INPUT);

  recieve = 0;

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
  
  //Remote zero
  if ((remote_map < 250) && (remote_map > 240)){
    remZero = 1;
  }else{
    remZero = 0;
  }
  //Local zero
  if ((local_map < 260) && (local_map > 240)){
    locZero = 1;
  }else{
    locZero = 0;
    recieve = 0;
  }
  //Remote con
  if(recieve == 1){
    Serial.print("REMOTE: ");
    Serial.println(remote_map);
    delay(500);
  }else if(recieve == 0){
    Serial.print("OVERRIDE, LOCAL: ");
    Serial.println(local_map);
    delay(500);
  }

  if ((locZero == 1) && (btnState == LOW)){
    recieve = 1;
  }
}

//TBD, Tähän koodi moodille jossa lisätty erillinen hätäseis (sama kuin 1 moodi, lisää tarkistus onko hätäseis painettu)
void mode2(){

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

  emgBtnState = digitalRead(emgBtn);

  if((emgBtnState == LOW) && (lastState == 1)){
    delay(300);
    emgState = 0;
    lastState = !lastState;
  } else if((emgBtnState == LOW) && (lastState == 0)){
    delay(300);
    emgState = 1;
    recieve = 0;
    lastState = !lastState;
  }

  if (emgState == 0){
    digitalWrite(emgLed, HIGH);
  }else{
    digitalWrite(emgLed, LOW);
  }
  btnState = digitalRead(override_btn);

  //Incoming
  remIn = analogRead(VRY1);
  locIn = analogRead(VRY2);

  //Mapping joysticks
  remote_map = map(remIn, 0, 1024, 0, 512);
  local_map = map(locIn, 0,1024, 0, 512);
  
  //Remote zero
  if ((remote_map < 260) && (remote_map > 240)){
    remZero = 1;
  }else{
    remZero = 0;
  }
  //Local zero
  if ((local_map < 260) && (local_map > 240)){
    locZero = 1;
  }else{
    locZero = 0;
    recieve = 0;
  }
  //Remote con
  if(recieve == 1){
    Serial.print("REMOTE: ");
    Serial.println(remote_map);
    delay(500);
  }else if(recieve == 0){
    Serial.print("OVERRIDE, LOCAL: ");
    Serial.println(local_map);
    delay(500);
  }
  //If handles are at 0, emgegency button is not pressed and override button is pressed transfer control
  if ((locZero == 1) && (remZero == 1) && (btnState == LOW) && (emgState == 0)){
    recieve = 1;
  }

}

//TBD, Tähän koodi mahdolliselle kolmannelle vaihtoehdolle
void mode3(){


}


void loop() {

  //Mode logic
  modeState = digitalRead(modeBtn);
  if(modeState == LOW){
    delay(500);
    currentMode++;
    if(currentMode > 3){
      currentMode = 1;
    }
    printedModeChangeMsg = false;
  }
  

  switch (currentMode){
    case 1:
      if(!printedModeChangeMsg){
        Serial.println("MODE 1");
      }
      printedModeChangeMsg = true;
      mode1();
      break;
    case 2:
      if(!printedModeChangeMsg){
        Serial.println("MODE 2");
      }
      printedModeChangeMsg = true;
      mode2();
      break;
    case 3:
      if(!printedModeChangeMsg){
        Serial.println("MODE 3");
      }
      printedModeChangeMsg = true;
      mode3();
      break;
    default:
      mode1();
      break;
  }

}
