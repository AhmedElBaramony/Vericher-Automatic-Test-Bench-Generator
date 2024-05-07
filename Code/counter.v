module counter(input clk,input load,input [4:0] in,input updown, output reg [4:0] counter,output reg high,output reg low);


always @(posedge clk) begin
    if(load)
    counter<=in;
    else if (updown) begin
        counter<=counter+5'b1;
    end
    else
    counter<=counter-5'b1;
end
    assign low=(counter==5'b0);
    assign high=(counter==5'b11111);

endmodule