- # Transmission Line Impedance Equations
  
For a transmission line of length $l$ , characteristic impedance $Z_0$ ,
propagation constant $\beta$ , and terminated with load $Z_L$ :  
  
$$
Z_{\text{in}} = Z_0 \frac{Z_L + j Z_0 \tan(\beta l)}{Z_0 + j Z_L \tan(\beta l)}
$$  
  
where:  

- $Z_{\text{in}}$ = input impedance
- $Z_0$ = characteristic impedance
- $Z_L$ = load impedance
- $\beta = \frac{2\pi}{\lambda}$ = phase constant
- $l$ = physical length of line
  
---

- ## Special Cases

- ### Short-Circuit Load ( $Z_L = 0$ )

  $$
  Z_{\text{in}} = j Z_0 \tan(\beta l)
  $$  

- ### Open-Circuit Load ( $Z_L \to \infty$ )

  $$
  Z_{\text{in}} = -j Z_0 \cot(\beta l)
  $$  

- ### Quarter-Wavelength Line ( $l = \lambda/4$ )

  $$
  Z_{\text{in}} = \frac{Z_0^2}{Z_L}
  $$  

- ### Half-Wavelength Line ( $l = \lambda/2$ )

  $$
  Z_{\text{in}} = Z_L
  $$  
-
  id:: 68b33066-19d8-41b0-b9d5-bb9e52abe023
-

- ### Microstrip lines
 	- Microstrip lines are a copper wire over a substrate. It has a GND plane in the back
 	- ![screenshot_30082025_104813.jpg](../assets/screenshot_30082025_104813_1756561708404_0.jpg)
 	- This is the  magnetic and electrical field of the microstrip line.
   id:: 68b3012f-d803-4ec0-8a14-64ede9ffb9bb
 	-
 	- How much the velocity of an electromagnetic wave slows down in a medium is:
   id:: 68b3042d-75da-478e-8430-18c35f3a3740
 	-

$$
   v = \frac{c}{\sqrt{\varepsilon_r}}
   $$ - $v$ = wave velocity in the medium
 - $c$ = speed of light in vacuum ( $\approx 3 \times 10^8 \, \text{m/s}$ )
 - $\varepsilon_r$ = relative permittivity (also called the dielectric constant) of the material
-
 - In a microstrip line, you can see that the $\varepsilon_r$ varies between the air and the substrate. Meaning that you'll have a $\varepsilon_{eff}$ , that is kinda of a average between both mediums
 -
 - # Wavelength Equations
     
   The **free-space wavelength** is:  
     
   $$
   \lambda_0 = \frac{c}{f}
   $$  
     
   where:  
 - $c \approx 3 \times 10^8 \, \text{m/s}$ = speed of light in vacuum
 - $f$ = frequency (Hz)
     
---
     
   When a wave propagates in a dielectric substrate with **effective dielectric constant** $\varepsilon_\text{eff}$ ,
   the wave velocity becomes:  
     
   $$
   v = \frac{c}{\sqrt{\varepsilon_\text{eff}}}
   $$  
     
   Thus, the **guided wavelength** is:  
     
   $$
   \lambda_g = \frac{v}{f} = \frac{\lambda_0}{\sqrt{\varepsilon_\text{eff}}}
   $$  
     
---
 -
 - ## How are Microstrip lines important
  - You have to calculate $Z_0$ . Because it's the characteristic impedance. After you have it, then you can check what are your $\varepsilon_r$ and $\varepsilon_{eff}$
  - With your $\varepsilon_{eff}$ in hand, you can calculate your real wave length $\lambda_{g}$
  -
  - The wave shortens inside the substrate, this is important to calculate matching impedance
  -
  -
  -
  -
 -
- ## Scattering params
 - You can only measure powere
-
