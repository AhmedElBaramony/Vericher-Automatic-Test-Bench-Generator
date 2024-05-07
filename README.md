
# Vericher Automatic Test Bench Generator

## Overview
Vericher is an advanced Automatic Test Bench Generator aimed at automating the verification of Verilog-based Digital Under Test (DUT). The tool streamlines the generation of robust test benches by automating the parsing of Verilog code, generating stimuli, and writing test benches that are ready for simulation. This project enhances the efficiency and dependability of digital system verifications, transforming the landscape of digital verification through automation.

## Features
- **Verilog Parser:** Parses the DUT’s Verilog code to extract input/output ports, variables, and control flow structures.
- **Stimulus Generator:** Generates various stimuli to test all possible combinations of inputs, ensuring comprehensive coverage and detecting potential design flaws.
- **Test Bench Writer:** Automatically writes test benches including initialization blocks, clock generation, and test case instantiation, providing ready-to-use scripts for simulation.
- **Automation of Verification Process:** Fully automates the generation of test benches, significantly reducing manual effort and improving the accuracy of the test process.

## Technical Architecture
- **Parser:** Utilizes regular expressions to extract essential data from Verilog code. Handles different aspects like module declarations, port definitions, and control flow statements.
- **Stimulus Generator:** Based on parser outputs, it creates varied and exhaustive test cases to simulate real-world scenarios and edge conditions.
- **Test Bench Writer:** Compiles the test bench code integrating inputs from the parser and stimulus generator, ensuring that the output is ready for simulation in environments like Questa-Sim.

## Usage
1. **Prepare Your Verilog Files:** Ensure your Verilog files are in the designated directory.
2. **Run the Parser:** Execute the parser with the Verilog file to extract necessary data.
3. **Generate Stimuli:** Use the stimulus generator to create input scenarios for your tests.
4. **Generate Test Bench:** Run the test bench writer to produce the test bench scripts.
5. **Simulate:** Use a compatible simulator to run the test benches and verify the DUT.

## Conclusion
The Vericher Automatic Test Bench Generator represents a significant step forward in the automation of digital verification, offering a tool that increases efficiency, reduces error rates, and accelerates the verification process.
