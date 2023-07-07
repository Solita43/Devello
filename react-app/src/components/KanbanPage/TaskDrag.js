import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Droppable, Draggable } from "react-beautiful-dnd"
import { taskPost } from "../../store/boardTasks";

function TaskDrag({ taskOrder, column }) {
    const [inFocus, setInFocus] = useState(false);
    const [newTask, setNewTask] = useState('');
    const tasks = useSelector(state => state.boardTasks)

    const dispatch = useDispatch();

    const handleClick = (e) => {

        e.preventDefault();
        window.alert("Feature Coming Soon...")
    }

    useEffect(() => {
        if (inFocus) document.getElementById("add-task").focus()
    }, [inFocus])

    const handleInputBlur = () => {
        // Send the updated information to the database
        if (!setNewTask) return 
        else {
            dispatch(taskPost({
                details: newTask,
                status: "Not started"
            }, column)).then((data) => {
                taskOrder.push(Object.keys(data)[0])
                setInFocus(false)
                setNewTask("")
            })
            
        }
    };

    const handleInputKeyPress = (event) => {
        if (event.key === 'Enter') {
            event.target.blur();
        }
    };

    if (!tasks || !taskOrder || !taskOrder.length) {
        return (
            <Droppable droppableId={`${column}`} type="task">
                {(provided, snapshot) => {
                    return (
                        <>
                            <div className="card-info-wrapper" ref={provided.innerRef} {...provided.droppableProps} style={{ backgroundColor: snapshot.isDraggingOver ? '#f5c1c8' : 'var(--white-background)', paddingTop: "0" }}>
                                {provided.placeholder}
                            </div>
                            <button className="add-task" onClick={handleClick}><i className="fa-solid fa-plus"></i> Add new task</button>
                        </>
                    )
                }}
            </Droppable>

        )
    }
    return (
        <Droppable droppableId={`${column}`} type="task">
            {(provided, snapshot) => {
                return (
                    <>
                        <div className="card-info-wrapper" ref={provided.innerRef} {...provided.droppableProps} style={{ backgroundColor: snapshot.isDraggingOver ? '#f5c1c8' : 'var(--white-background)' }}>
                            {taskOrder.length && taskOrder.map((taskId, index) => {
                                const task = tasks[taskId];
                                if (!task) return null;
                                return (
                                    <Draggable key={task.id} draggableId={`task-${task.id}`} index={index}>
                                        {(provided) => (
                                            <div key={task.id} className="kanban-task-container" ref={provided.innerRef}
                                                {...provided.draggableProps}
                                                {...provided.dragHandleProps}
                                                onClick={handleClick}>
                                                <p className="task-details"><i className="fa-regular fa-circle-check"></i> {task.details}</p>
                                            </div>
                                        )}
                                    </Draggable>
                                )
                            })}
                        {inFocus ? (<div className="kanban-task-container"><i className="fa-regular fa-circle-check"></i><input
                            type="text"
                            value={newTask}
                            maxLength={20}
                            minLength={1}
                            onChange={(e) => setNewTask(e.target.value)}
                            onBlur={handleInputBlur}
                            onKeyPress={handleInputKeyPress}
                            className="task-details"
                            id="add-task"
                            placeholder="New Task"

                        /></div>) : null}

                        <button className="add-task" onClick={() => setInFocus(true)}><i className="fa-solid fa-plus"></i> Add new task</button>
                            {provided.placeholder}
                        </div>
                    </>
                )
            }}

        </Droppable>
    )
}

export default TaskDrag;