function [vtc_s, bc_s] = get_vtc_series(cop, bos, fs)
    % Get VTC and BC time-series
    % Params:
    %   cop: anterior-posterior and medio-lateral CoP data | EasyDict of np.array
	%   bos: base of support | EasyDict of list
	%   fs: sampling rate (Hz) | int/float
    % Returns
    %   vtc_s: VTC time series | np.array
	%   bc_s: BC time series | np.array
    
    A_VERY_LARGE_NUMBER = 999;

    ts = 1.0/fs;
    rx = cop.x;
    ry = cop.y;
    vx = diff(rx)./ts;
    vy = diff(ry)./ts;
    ax = diff(vx)./ts;
    ay = diff(vy)./ts;

    s_size = length(ax);
    vtc_s  = A_VERY_LARGE_NUMBER*ones(1, s_size);
    bc_s   = A_VERY_LARGE_NUMBER*ones(1, s_size);

    disp('* Start the VTC calculation')
    for i = 1:s_size
        r = [rx(i + 2), ry(i + 2)];
        v = [vx(i + 1), vy(i + 1)];
        a = [ax(i), ay(i)];

        tau_AB = get_vtc(r, v, a, bos.A, bos.B);
        tau_BC = get_vtc(r, v, a, bos.B, bos.C);
        tau_CD = get_vtc(r, v, a, bos.C, bos.D);
        tau_DA = get_vtc(r, v, a, bos.D, bos.A);

        all_tau  = [tau_AB, tau_BC, tau_CD, tau_DA];
        vtc_s(i) = min(all_tau);
        min_id   = find(all_tau == min(all_tau));
        bc_s(i)  = mod(min_id, 2);
    end
end