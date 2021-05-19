package com.example.lr1_maket;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.EditText;
import android.widget.TextView;

public class sign extends AppCompatActivity {
   /* private EditText namereg;
    private EditText emailreg;
    private EditText firstpas;
    private EditText secondpas;*/
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sign);

        Intent intent = getIntent();
        String getMsg = intent.getStringExtra("namereg");
        TextView signTxt = (TextView) findViewById(R.id.signTxt);
        signTxt.setText(getMsg);
        /*namereg= (EditText) findViewById(R.id.namereg);
        emailreg= (EditText) findViewById(R.id.emailreg);
        firstpas=(EditText) findViewById(R.id.firstpas);
        secondpas= (EditText) findViewById(R.id.secondpas);*/

    }
}