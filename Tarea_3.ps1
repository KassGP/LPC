function cuadrado{
    $re = $n*$n
    "Cuadrado: "+$re
}
function cubo{
    $re = [math]::Pow($n, 3)
    "Cubo: "+$re
}
 function raiz{
    $re = [math]::Sqrt($n)
    "Raiz: "+$re
}
clear
function opciones{
    Write-Host "---- Opciones ----"
    Write-Host "Seleccione la operación a realizar"
    Write-Host "Presione 1 para elevarlo al cuadrado"
    Write-Host "Presione 2 para elevarlo al cubo"
    Write-Host "Presione 3 para sacar su raiz"
    Write-Host "Presione 0 para salir"
}
do{
    "Operaciones"
    $n = read-Host "Ingrese un numero"
    Opciones
    $input = Read-Host "Seleccione la opcion que desee"
    clear
    switch($input){
        '1'{
            cuadrado
            
        }
        '2'{
            cubo
              
        }
        '3'{
            raiz
            
        }'0'{
            
            $quit = "0"
        }
    }
    
}Until ($quit -eq "0")
clear
Write-Host "Nos vemos :)"