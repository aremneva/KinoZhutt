package com.example.lr1_maket;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

public class reg extends AppCompatActivity {

    public EditText namereg;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_reg);



        /*Intent intent = new Intent (this,reg.class);
        */
        namereg=(EditText) findViewById(R.id.namereg);

        //
    }

    public void onclicked(View view) {
        Intent intent = new Intent(this, MainActivity.class);
        startActivity(intent);

    }

    public void create(View view) {
        Intent intent = new Intent(this, sign.class);
        String txtnamereg = getIntent().getStringExtra("namereg").toString();
        intent.putExtra("amereg", txtnamereg);
        startActivity(intent);


       //intent.putExtra("namereg")
    }
}