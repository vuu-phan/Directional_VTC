% name: main.py
% description: directional VTC calculation
% author: Vu Phan
% date: 2023/07/22


clear
close all
clc

% Constants
IDX = 2;
IDY = 3;
fs = 2000; % Hz

% Boundary
% YOU NEED TO MEASURES BOS OF YOUR PARTICIPANT AND ENTER IT HERE -->
bos   = struct();
bos.A = [10, -10];
bos.B = [15, 20];
bos.C = [-15, 20];
bos.D = [-10, -10];
% <-- YOU NEED TO MEASURES BOS OF YOUR PARTICIPANT AND ENTER IT HERE

% Get CoP data
dt = readmatrix("../data/sample_cop.csv");

cop   = struct();
cop.x = dt(:, IDX);
cop.y = dt(:, IDY);

% Obtain VTC time-series
[vtc_s, bc_s] = get_vtc_series(cop, bos, fs);

% Calculate directional VTC outcomes
[outcomes] = get_vtc_outcomes(vtc_s, bc_s, fs);

fprintf("2D VTC mean = %.2f (s)\n", outcomes(1));
fprintf("AP VTC mean = %.2f (s)\n", outcomes(2));
fprintf("ML VTC mean = %.2f (s)\n", outcomes(3));
fprintf("AP BC = %.2f (percents) \n", outcomes(4));
fprintf("ML BC = %.2f (percents) \n", outcomes(5));
fprintf("Switching rate = %.2f (Hz)\n", outcomes(6));