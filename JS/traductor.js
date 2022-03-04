function translate(str){
    let translation = str;
    // si la palabra termina en "ar", se le quitan esos dos ultimos caracteres
    if (str.toLowerCase().endsWith('ar')){
        translation = str.slice(0,-2); 
        // corta desde l inicio hasta los ultimos dos
    }

    // Si la palabra inicia con "Z" se le añade "pe" al final

    if(str.toLowerCase().startsWith('z')){
        translation += 'pe';
    }

    // Si la palabra tiene 10 o más letras, se parte a la mitad y se divide con "-"

    const lengthl = translation.length
    if(lengthl >= 10){
        const fst = translation.slice(0, Math.round(lengthl / 2))
        const snd = translation.slice(Math.round(lengthl / 2))

        translation =  `${fst}-${snd}`
    }

    // Si la palabra original es un palindromo entonces ninguna anterior cuenta y se devuelve la misma palabra intercalando mayusculas y minusculas
    const reverse = (str) => str.split('').reverse().join('') 
    //str.split('') devuelve la palabra dividida por cada caracter
    function minMay(str){
        const length = str.length
        let translation = ''
        let capitalize = true

        for (let i = 0; i < length; i++ ){
            const char = str.charAt(i)

            translation += capitalize ? char.toUpperCase() : char.toLowerCase()
            capitalize = !capitalize
            
        }
        return translation
    }

    if(str == reverse(str)){
        return minMay(str)
    }
    return translation
    

}