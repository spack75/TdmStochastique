%

clear all;
close all;

data = load('../data/data_markov.txt');
I_max = data(:,1);

cpt_1 = 0;
cpt_2 = 0;
cpt_3 = 0;
cpt_inf_10 = 0;

for i = 1:size(data,1)
  switch I_max
    case 1
      cpt_1 = cpt_1 + 1;
     case 2
      cpt_1 = cpt_2 + 2;
     case 3
      cpt_1 = cpt_1 + 3;
  endswitch
  
  if I_max <= 10
    cpt_inf_10  = cpt_inf_10 + 1;
  endif
end


