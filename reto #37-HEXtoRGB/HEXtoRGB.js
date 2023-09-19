function hexToRgb(hex) {
    return{
        red: hex >> 16,
        green: hex >> 8 & 255,
        blue: hex & 255
    };
}

let colorHex = 0xFFFFFF;
let colorRgb = hexToRgb(colorHex);
console.log(`Color Hexadecimal ${colorHex}`); // Color hexadecimal #ffffff

console.log();

colorHex = 0x372554;
colorRgb = hexToRgb(colorHex);
console.log(`Color Hexadecimal ${colorHex}`);// Color hexadecimal #372554