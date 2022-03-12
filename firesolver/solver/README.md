WILDFIRE CAUSES:
<https://www.for.gov.bc.ca/ftp/!Project/FireBehaviour/Canadian%20Fire%20Behaviour%20for%20AU/FWI%20Tables.pdf>

    * 45% of all wildfires are caused by lightnting -> Lightning needs foliage density to ignite
    * effective rainfall -> Pe = 0.92 * P -1.27, for P > 1.5
    * duff moisture content ->DMC =244.72−43.43⋅ln(M−20) ->   M = 1000Pe / 48.77 + b * Pe -> b = 0.5 constant because it depends on previous day
    * moisture equivelent -> Q = 3.937 * Pe 
    * Drought code ->  DC = 400 * ln(800 /Q)
    * Average wind speed  = ~ 10Kph or ~ 15Mph or ~ 6m/s 
    * wind function -> f(U) = e ^ (0.05039) * 
    tentative metric:
        M[i,j] = 0.7 * Ave_Foliage(i,j) / Max(foliage) + 0.35(Ave_tamp / Max(Ave_temp)) + (0.1)* (ave_fireworks / Maxfireworks) 
        + 0.8 (DMC[i, j]) + 0.7 (DC)
