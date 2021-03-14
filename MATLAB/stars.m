%% 
% 1.Variables

spectra = importdata('spectra.csv');
starNames = importdata('star_names.csv');
lambdaStart = importdata('lambda_start.csv');
lambdaDelta = importdata('lambda_delta.csv');
%% 
% 2. The number of observations

num_names = size(starNames, 1);
num_obs = size(spectra, 1);
%% 
% 3. Vector *lambda*

lambda = [lambdaStart : lambdaDelta : lambdaDelta * (num_obs - 1) + lambdaStart]';
%% 
% 4. Minimum Intensivity

min_intens(num_names, 1) = struct('name', '', 'min_intense', 0, 'index', 0 );
for i = 1 : 1 : num_names 
    min_intens(i).name = string(starNames(i));
    [min_intens(i).min_intense, min_intens(i).index] = min(spectra(: , i));
end
%% 
% 5. Speed

speed = zeros(num_names, 1);
fig = figure;
hold on;
grid on;
c = physconst('LightSpeed');
lambdaH = 656.28;
for i = 1 : 1 : num_names 
    speed(i) = c * (lambda(min_intens(i).index) / lambdaH - 1);
    if (speed(i) < 0)
        p = plot(lambda, spectra(:, i),'--','Color',[rand(1) rand(1) rand(1)]);
        p.LineWidth = 1;
    else
        p = plot(lambda, spectra(:, i), 'Color',[rand(1) rand(1) rand(1)]);
        p.LineWidth = 3; 
    end
end
%% 
% 7. Plots

xlabel('Длина волны, нм');
ylabel(['Интенсивность, эрг/см^2/с/', char(197)]);
title('Спектры звезд');
legend(starNames);
set(fig, 'Visible', 'on'); 
text((lambdaStart + (max(lambda) - lambdaStart) / 4), 3.25 * 10^-13,'Алпатова Полина Б01-009')
saveas(fig, 'grafic.png');
%% 
% 8. Movaway stars

movaway = starNames(speed > 0);