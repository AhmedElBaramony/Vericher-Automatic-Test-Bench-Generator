module fulladder_tb;

  //INPUTS
    reg X;
   reg Y;
   reg Ci;

  //OUTPUTS
    wire Co;
 wire S;

  //INISTANCE
  fulladder T (.X (X),.Y (Y),.Ci (Ci),.Co (Co),.S (S));



  initial begin
    // Run the simulation for a specific time

    #10 X = 0;Y = 0;Ci = 0;
   #10 X = 0;Y = 0;Ci = 1;
   #10 X = 0;Y = 1;Ci = 0;
   #10 X = 0;Y = 1;Ci = 1;
   #10 X = 1;Y = 0;Ci = 0;
   #10 X = 1;Y = 0;Ci = 1;
   #10 X = 1;Y = 1;Ci = 0;
   #10 X = 1;Y = 1;Ci = 1;


    // End the simulation
    $stop;
  end

endmodule