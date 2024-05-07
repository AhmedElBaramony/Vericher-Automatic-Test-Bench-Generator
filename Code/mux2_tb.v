module mux2_tb;

  //INPUTS
    reg A;
   reg B;
   reg S;

  //OUTPUTS
    wire O;

  //INISTANCE
  mux2 T (.A (A),.B (B),.S (S),.O (O));



  initial begin
    // Run the simulation for a specific time

    #10 A = 0;B = 0;S = 0;
   #10 A = 0;B = 0;S = 1;
   #10 A = 0;B = 1;S = 0;
   #10 A = 0;B = 1;S = 1;
   #10 A = 1;B = 0;S = 0;
   #10 A = 1;B = 0;S = 1;
   #10 A = 1;B = 1;S = 0;
   #10 A = 1;B = 1;S = 1;


    // End the simulation
    $stop;
  end

endmodule