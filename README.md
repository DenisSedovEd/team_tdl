

## Таблицы базы данных

### Users:
```
 User {
    username: str
    email: email
    password: pass
    position: str
    status: str
    name: str
    lastname: str
 }
  list_task {
    title: str
    tasks: Task
 }
 task{
    title: str
    parrent_task: ForiengKey
    status: STATUS_TASK
 }
```