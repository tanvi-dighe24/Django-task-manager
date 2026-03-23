// JavaScript: Handling Task Interactions

document.addEventListener('DOMContentLoaded', () => {
    const taskList = document.getElementById('task-list');

    // 1. Toggle Task Completion
    taskList.addEventListener('click', (e) => {
        if (e.target.tagName === 'SPAN') {
            e.target.classList.toggle('completed');
            console.log("Task status toggled locally.");
        }
    });

    // 2. Delete Task with Animation
    const deleteButtons = document.querySelectorAll('.delete-btn');
    
    deleteButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            const taskItem = e.target.parentElement;
            
            if (confirm('Are you sure you want to remove this task?')) {
                // Simple fade-out effect
                taskItem.style.opacity = '0';
                setTimeout(() => {
                    taskItem.remove();
                }, 300);
                console.log("Task removed from the UI.");
            }
        });
    });
});