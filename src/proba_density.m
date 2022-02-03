function [P] = proba_density(U,N)
  % This function takes a signal vector and number of band + 1,
  % and return his probability density
  % U : signal vector
  % N : number of band + 1
  % P : probability density
  
  dh = (max(U) - min(U))/N;     % band step
  
  cpt = zeros(N);
  for i = [1:length(U)]
   band = floor((U(i) - min(U))/dh) + 1;      % band = in which band is u(i), n°1,2...
   cpt(band) = cpt(band) + 1;                 % how many point there is in each band
  end
  for i = 1:N
    P(i) = cpt(i)/(dh*length(U));             % Probability density
  endfor
  
  plot(band,P);
  
  % plotting graphics and normal function
  %x = linspace(min(U),max(U),N);
  %ecart_type = sqrt(mean(U - mean(U)).^2);
end