
void setup() {
  Serial.begin(9600);
  
 
}

void loop() {
 float Ozone = 0;
 float NO2 = 0;
 float NH3 = 0;
 float CO =0;  
  Ozone = analogRead(A0);
  NO2 = analogRead(A1);
  NH3 = analogRead(A2);
  CO = analogRead(A3);
  Serial.println("ozone:");
  Serial.println(Ozone,DEC);
  Serial.println("NO2:");
  Serial.println(NO2);
  Serial.println("NH3");
  Serial.println(NH3);
  Serial.println("CO:");
  Serial.println(CO);
   Serial.println("----------------");
  delay(3000);
  
  

}
