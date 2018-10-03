uint32_t SLEEP_TIME = 30000; 
float Ro = 10000.0;    
int val = 0;           
float valMQ =0.0;
float lastMQ =0.0;
float           LPGCurve[3]  =  {2.3,0.21,-0.47};   
float           COCurve[3]  =  {2.3,0.72,-0.34};   
float           SmokeCurve[3] = {2.3,0.53,-0.44};   


void setup()
{
    Ro = MQCalibration(
             A2);         //Calibrating the sensor. Please make sure the sensor is in clean air
}

void loop()
{
    uint16_t valMQ = MQGetGasPercentage(MQRead(A2)/Ro,GAS_CO);
    Serial.println(val);

    Serial.print("LPG:");
    Serial.print(MQGetGasPercentage(MQRead(A2)/Ro,GAS_LPG) );
    Serial.print( "ppm" );
    Serial.print("    ");
    Serial.print("CO:");
    Serial.print(MQGetGasPercentage(MQRead(A2)/Ro,GAS_CO) );
    Serial.print( "ppm" );
    Serial.print("    ");
    Serial.print("SMOKE:");
    Serial.print(MQGetGasPercentage(MQRead(A2)/Ro,GAS_SMOKE) );
    Serial.print( "ppm" );
    Serial.print("\n");

    if (valMQ != lastMQ) {
        send(msg.set((int16_t)ceil(valMQ)));
        lastMQ = ceil(valMQ);
    }

    sleep(SLEEP_TIME); //sleep for: sleepTime
}


float MQResistanceCalculation(int raw_adc)
{
    return ( ((float)RL_VALUE*(1023-raw_adc)/raw_adc));
}


float MQCalibration(int mq_pin)
{
    int i;
    float val=0;

    for (i=0; i<CALIBARAION_SAMPLE_TIMES; i++) {          
        val += MQResistanceCalculation(analogRead(A2));
        delay(CALIBRATION_SAMPLE_INTERVAL);
    }
    val = val/CALIBARAION_SAMPLE_TIMES;                   

    val = val/RO_CLEAN_AIR_FACTOR;                        
    return val;
}
float MQRead(int mq_pin)
{
    int i;
    float rs=0;

    for (i=0; i<READ_SAMPLE_TIMES; i++) {
        rs += MQResistanceCalculation(analogRead(A2));
        delay(READ_SAMPLE_INTERVAL);
    }

    rs = rs/READ_SAMPLE_TIMES;

    return rs;
}


int MQGetGasPercentage(float rs_ro_ratio, int gas_id)
{
    if ( gas_id == GAS_LPG ) {
        return MQGetPercentage(rs_ro_ratio,LPGCurve);
    } else if ( gas_id == GAS_CO ) {
        return MQGetPercentage(rs_ro_ratio,COCurve);
    } else if ( gas_id == GAS_SMOKE ) {
        return MQGetPercentage(rs_ro_ratio,SmokeCurve);
    }

    return 0;
}

int  MQGetPercentage(float rs_ro_ratio, float *pcurve)
{
    return (pow(10,( ((log(rs_ro_ratio)-pcurve[1])/pcurve[2]) + pcurve[0])));
}
