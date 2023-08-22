const randWords = ["autopista","camión","coche","rueda", "estacionamiento", "tren", "transito", "faros", "capot", "parabrisas"];

const getRandom = (length) => Math.floor(Math.random() * length);


const sixtyPercent = (word) => Math.floor(60 * word.length / 100);


const getIndexLists = (word, nchars) => {
    let indexSet = new Set();

    while (indexSet.size < nchars) {
        indexSet.add(getRandom(word.length));
    }

    let notShownIndex = [];
    for (let i=0; i<word.length; i++) {
        if (![...indexSet].includes(i)) {
            notShownIndex.push(i);
        }
    }

    return [[...indexSet], notShownIndex];
};


const showWord = (word, indexList) => {
    let result = '';

    word.split('').forEach((char, idx) => {
        if (indexList.includes(idx)) result += char;
        else result += '_';
    });

    console.log(result);
};


function playGame(){
    const randWord = randWords[getRandom(randWords.length)];

    let [showIndexList, notShownIndex] = getIndexLists(randWord, sixtyPercent(randWord));
    
    let attempts = 4;           // number of attempts to guess the word
    let userWins = false;
    
    console.log('Try to guess the word:');
    while (attempts && !userWins) {
        showWord(randWord, showIndexList);

        let userInput = prompt('Enter a letter or a word: ');
        userInput = userInput.toLowerCase();
        
        if (userInput.length !== 1 && userInput.length !== randWord.length) {
            attempts--;
            console.log('\nYou can only enter one letter or the whole word!\n');
            console.log(`number of attempts left: ${attempts}`);
            continue;
        }
        
        if (userInput.length === 1){
            let includesChar = false;

            notShownIndex.slice().forEach(idx => {
                if (userInput === randWord[idx]) {
                    showIndexList.push(idx);
                    notShownIndex.splice(notShownIndex.indexOf(idx), 1);
                    includesChar = true;
                }
            });

            if (!includesChar) {
                attempts--;
                console.log(`number of attempts left: ${attempts}`);
            }

        } else {
            if (userInput !== randWord) {
                attempts--;
                console.log(`number of attempts left: ${attempts}`);
            } else {
                userWins = true;
                break;
            }
        }

        // condition for winning
        if (showIndexList.length === randWord.length) {
            userWins = true;
        }
    }

    console.log(`\nThe word is: ${randWord.toUpperCase()}`);

    if (userWins) {
        console.log('You Win!');
    } else {
        console.log('You lose...');
    }
}

playGame();