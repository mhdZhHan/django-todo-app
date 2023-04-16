window.addEventListener('load', ()=>{
    // const inputBox = document.getElementById("input")
    // const addBtn = document.getElementById("add_btn")

    // const todoList = document.getElementById('tasks')
    // const completedTodoList = document.getElementById('completed_tasks')

    // let tasks = [
    //     {
    //         id: 1,
    //         task: 'Helloooo',
    //         isDone: true,
    //     }
    // ]

    // if(tasks.length !== 0){
    //     renderTodoList()
    // }


    // addBtn.addEventListener('click', function() {
    //     let inputValue = inputBox.value
    //     if (inputValue !== "") {
    //         let newTask = {
    //             id: Date.now(),
    //             task: inputValue,
    //             isDone: false,
    //         }
    //         inputBox.value = ''
    //         tasks = [...tasks, newTask]
    //         renderTodoList()
    //     }
    // })

    // // delete undo check
    // function todoSettings(event){
    //     const target = event.target
    //     if (target.classList.contains('circle')) {
    //         const taskId = parseInt(target.getAttribute('task_id'))
    //         let task = tasks.find(task => task.id === taskId)
    //         task.isDone = !task.isDone
    //         renderTodoList()
    //     }else if (target.classList.contains('delete')){
    //         const taskId = parseInt(target.getAttribute('task_id'))
    //         const taskIndex = tasks.findIndex(task => task.id === taskId)
    //         tasks.splice(taskIndex, 1)
    //         renderTodoList()
    //     }else if(target.classList.contains('undo')){
    //         const taskId = parseInt(target.getAttribute('task_id'))
    //         let task = tasks.find(task => task.id === taskId)
    //         console.log(taskId);
    //         task.isDone = !task.isDone
    //         renderTodoList()
    //     }
    // }
    
    // todoList.addEventListener('click', todoSettings)

    // completedTodoList.addEventListener('click', todoSettings)
    
    // function renderTodoList() {
    //     console.log(tasks)
    //     let task_item = ''
    //     todoList.innerHTML = ''
    //     completedTodoList.innerHTML = ''
    //     tasks.map((task)=>{
    //         task_item = `
    //             <li class="item" task_id="${task.id}">
    //                 <div class="left">
    //                     ${
    //                         task.isDone ? 
    //                             `<span class="check" id="check">
    //                                 <img src="${checkImg}" alt="check" />
    //                             </span>`
    //                         : `<span task_id="${task.id}" class="circle"></span>`
    //                     }
    //                     <span class="text">${task.task}</span>
    //                 </div>
    //                 <div class="right">
    //                     ${
    //                         task.isDone?
    //                             `<span class="undo" task_id="${task.id}">
    //                                 <img src="${undoImg}" class="undo" task_id="${task.id}" alt="undo" />
    //                             </span>`
    //                         : ``
    //                     }
    //                     <span class="delete" task_id="${task.id}">
    //                         <img src="${deleteImg}" class="delete" alt="delete" />
    //                     </span>
    //                 </div>
    //             </li>
    //         `
    //         if(task.isDone){
    //             completedTodoList.innerHTML += task_item
    //         } else {
    //             todoList.innerHTML += task_item
    //         }
    //     })
    // }

    // const circle_btns = document.querySelectorAll('.circle')    

    // circle_btns.forEach((btn)=>{
    //     btn.addEventListener('click', function(event){
    //         event.preventDefault()
    //         let taskId = this.getAttribute("data_task_id");
    //         console.log(taskId);
    //         fetch("/complete/" + taskId + "/", {
    //             method: "POST",
    //             headers: {
    //                 "Content-Type": "application/json"
    //             },
    //         })
    //         .then(response => response.json())
    //         .then(data => {
    //             if (data.success) {
    //                 alert("Task updated successfully.")
    //                 location.reload();
    //             } else {
    //                 alert("Failed to update task.")
    //             }
    //         })
    //         .catch(error => {
    //             alert("Failed to update task.")
    //         })
    //     })
    // })

})