# ElVA AI Vacant position: Software Engineer 

# GeocodingProject


This project uses the Geocoding API to obtain coordinates and neighborhoods from addresses in Portland, Oregon.

## Dependencies

- [geopy](https://geopy.readthedocs.io/en/stable/): A Python library for performing geocoding and place searching.
- [Google Maps API](https://developers.google.com/maps/documentation/geocoding/start): Used to geocode addresses and obtain information about neighborhoods.

## Processes Performed

### 1. Initial Geocoding
    - **Initial Address:** 1300 SE Stark Street, Portland, OR 97214
    - **Initial Coordinates:** (45.518967950000004, -122.65214122044995)
    - **Initial Neighborhood:** No neighborhood found

### 2. Neighborhood Search
    - **Location:** I use the initial coordinates to search for nearby neighborhoods.

### 3. Recursive Function
    - I create a recursive function that increments the address number by 100 units and performs geocoding and neighborhood search.

### 4. Neighborhood Change
    - The function runs until the returned neighborhood is different from the initial neighborhood.

### 5. Final Result
    - The address that caused the neighborhood change was 1500 SE Stark Street, Portland, OR 97214.
    - The new neighborhood is University District.

## Tests Performed

1. Tests are carried out to verify the geocoding of the initial address.
2. The search for nearby neighborhoods was verified using the initial coordinates.
3. The recursive function was executed to increment addresses and check for neighborhood changes.

## Code Execution

  Install the dependencies and a valid API Key. Then, run the `geocoding_script.py` script.

```bash
python geocoding_script.py


uses the geopy library together with the OpenStreetMap geocoding service.

As in the previous code, this script performs the following actions:

Geocoding the initial address to obtain the coordinates.
Neighborhood query using initial coordinates (reverse geocoding).
Run a recursive function to increment the address by 100 and repeat steps 1 and 2 until the neighborhood changes.
This code uses the OpenStreetMap API via geopy.geocoders.Nominatim.


# ElVA AI Puesto vacante: Ingeniero de software

# Geocoding Project 


Este proyecto utiliza la API de geocodificación para obtener coordenadas y vecindarios a partir de direcciones en Portland, Oregon.

## Dependencias

- [geopy](https://geopy.readthedocs.io/en/stable/): Una biblioteca de Python para realizar geocodificación y búsqueda de lugares.
- [Google Maps API](https://developers.google.com/maps/documentation/geocoding/start): Se utiliza para geocodificar direcciones y obtener información sobre vecindarios.

## Procesos Realizados

### 1. Geocodificación Inicial
   - **Dirección Inicial:** 1300 SE Stark Street, Portland, OR 97214
   - **Coordenadas Iniciales:** (45.518967950000004, -122.65214122044995)
   - **Vecindario Inicial:** No se encontró vecindario

### 2. Búsqueda de Vecindario
   - **Ubicación:** Utilizo las coordenadas iniciales para buscar vecindarios cercanos.

### 3. Función Recursiva
   - Creo una función recursiva que incrementa el número de la dirección en 100 unidades y realiza geocodificación y búsqueda de vecindario.

### 4. Cambio de Vecindario
   - La función se ejecuta hasta que el vecindario devuelto es diferente al vecindario inicial.

### 5. Resultado Final
   - La dirección que provocó el cambio de vecindario fue 1500 SE Stark Street, Portland, OR 97214.
   - El nuevo vecindario es University District.

## Pruebas Realizadas

1. Se realiza pruebas para verificar la geocodificación de la dirección inicial.
2. Se verificó la búsqueda de vecindarios cercanos utilizando las coordenadas iniciales.
3. Se ejecutó la función recursiva para incrementar direcciones y verificar cambios de vecindario.

## Ejecución del Código

 Instaladar las dependencias y un API Key válido.Luego, ejecuta el script `geocoding_script.py`.

```bash
python geocoding_script.py


utiliza la biblioteca geopy junto con el servicio de geocodificación de OpenStreetMap.

Al igual que en el código anterior, este script realiza las siguientes acciones:

Geocodificación de la dirección inicial para obtener las coordenadas.
Consulta del vecindario utilizando las coordenadas iniciales (geocodificación inversa).
Ejecución de una función recursiva para incrementar la dirección en 100 y repetir los pasos 1 y 2 hasta que el vecindario cambie.
Este código utiliza la API de OpenStreetMap a través de geopy.geocoders.Nominatim. 