function [outcomes] = get_vtc_outcomes(vtc_s, bc_s, fs, varargin)
    % Obtain directional VTC measures
    % Params:
    %   vtc_s: time-series of VTC 
	%   bc_s: time-series of BC 
	%   varargin: self-defined threshold for calculating switching rate
    % Returns:
    %   outcomes: set of directional VTC measures 
    
    if (nargin > 3)
        threshold = varargin{1};
    else
        threshold = mean(vtc_s) + 3*std(vtc_s);
    end

    DIR_Y = 1;
    DIR_X = 0;

    num_samples = length(vtc_s);

    id_y = find(bc_s == DIR_Y);
    id_x = find(bc_s == DIR_X);

    vtc_2d = mean(vtc_s);
    vtc_y  = mean(vtc_s(id_y));
    vtc_x  = mean(vtc_s(id_x));

    bc_y = length(id_y)*100.0/num_samples;
    bc_x = length(id_x)*100.0/num_samples;

    [sr_p, ~] = findpeaks(vtc_s, 'MinPeakHeight', threshold);
    sr = length(sr_p)*fs/num_samples;

    outcomes = [vtc_2d, vtc_y, vtc_x, bc_y, bc_x, sr];
end