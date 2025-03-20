const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

const MAX_WIDTH = 600;
const MAX_HEIGHT = 400;

let player = {
    x: 50,
    y: MAX_HEIGHT - 40,
    width: 40,
    height: 40,
    isJumping: false,
    jumpCount: 10
};

let enemy = {
    x: MAX_WIDTH,
    y: MAX_HEIGHT - 40,
    width: 20,
    height: 40
};

let speed = 7;

function drawPlayer() {
    ctx.fillStyle = 'blue';
    ctx.fillRect(player.x, player.y, player.width, player.height);
}

function drawEnemy() {
    ctx.fillStyle = 'red';
    ctx.fillRect(enemy.x, enemy.y, enemy.width, enemy.height);
}

function moveEnemy() {
    enemy.x -= speed;
    if (enemy.x <= 0) {
        enemy.x = MAX_WIDTH;
    }
}

function jump() {
    if (player.isJumping) {
        if (player.jumpCount >= -10) {
            let neg = 1;
            if (player.jumpCount < 0) {
                neg = -1;
            }
            player.y -= player.jumpCount ** 2 * 0.7 * neg;
            player.jumpCount -= 1;
        } else {
            player.isJumping = false;
            player.jumpCount = 10;
        }
    }
}

function checkCollision() {
    if (
        player.x < enemy.x + enemy.width &&
        player.x + player.width > enemy.x &&
        player.y < enemy.y + enemy.height &&
        player.y + player.height > enemy.y
    ) {
        alert("Game Over!");
        resetGame();
    }
}

function resetGame() {
    player.x = 50;
    player.y = MAX_HEIGHT - 40;
    enemy.x = MAX_WIDTH;
    speed = 7;
}

function update() {
    ctx.clearRect(0, 0, MAX_WIDTH, MAX_HEIGHT);
    
    drawPlayer();
    drawEnemy();
    
    moveEnemy();
    jump();
    checkCollision();
    
    speed += 0.01;
    
    requestAnimationFrame(update);
}

document.addEventListener('keydown', (event) => {
    if (event.key === ' ' && !player.isJumping) {
        player.isJumping = true;
    }
});

update();
