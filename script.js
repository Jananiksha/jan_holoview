document.addEventListener('DOMContentLoaded', function() {
    const sliderContainer = document.querySelector('.slider-container');
    const ball = document.querySelector('.ball');
    let isDragging = false;
    
    ball.addEventListener('mousedown', function(event) {
        isDragging = true;
        const initialMouseX = event.clientX;
        const initialBallX = ball.offsetLeft;
        
        document.addEventListener('mousemove', dragBall);
        document.addEventListener('mouseup', releaseBall);
        
        function dragBall(event) {
            if (isDragging) {
                const offsetX = event.clientX - initialMouseX;
                const newBallX = initialBallX + offsetX;
                const minPosition = 0;
                const maxPosition = sliderContainer.offsetWidth - ball.offsetWidth;
                const boundedX = Math.max(minPosition, Math.min(maxPosition, newBallX));
                ball.style.left = boundedX + 'px';
            }
        }
        
        function releaseBall() {
            isDragging = false;
            document.removeEventListener('mousemove', dragBall);
            document.removeEventListener('mouseup', releaseBall);
        }
    });
});