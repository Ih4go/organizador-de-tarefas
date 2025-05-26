import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import json

class TaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rei do Pitaco - Organizador de Tarefas")
        self.save_file = "tasks.json"
        
        # Configurar estilo
        self.style = ttk.Style()
        self.style.configure("Header.TLabel", 
                           font=("Arial", 14, "bold"), 
                           foreground="#2c3e50",
                           background="#ecf0f1",
                           padding=10)
        
        self.style.configure("Footer.TLabel", 
                          font=("Arial", 8), 
                          foreground="#7f8c8d",
                          background="#bdc3c7",
                          padding=5)
        
        self.columns = [
            {"name": "Tarefas a Fazer", "color": "#FFCCCC", "tasks": []},
            {"name": "Em Andamento", "color": "#CCFFCC", "tasks": []},
            {"name": "Concluídas", "color": "#CCCCFF", "tasks": []}
        ]
        
        self.create_widgets()
        self.load_tasks()
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def create_widgets(self):
        # Cabeçalho
        header = ttk.Label(self.root, 
                         text="REI DO PITACO", 
                         style="Header.TLabel",
                         anchor="center")
        header.grid(row=0, column=0, columnspan=3, sticky="ew", padx=5, pady=5)
        
        # Colunas principais
        self.column_frames = []
        for i, column in enumerate(self.columns):
            frame = ttk.Frame(self.root, padding=5)
            frame.grid(row=1, column=i, padx=5, pady=5, sticky="nsew")
            
            header_col = ttk.Label(frame, 
                                 text=column["name"], 
                                 background=column["color"],
                                 font=("Arial", 10, "bold"))
            header_col.pack(fill="x", pady=5)
            
            container = ttk.Frame(frame)
            container.pack(fill="both", expand=True)
            
            self.column_frames.append({"frame": frame, "container": container})
            self.root.columnconfigure(i, weight=1)
        
        # Botão de adicionar
        add_button = ttk.Button(self.root, 
                              text="+ Nova Tarefa", 
                              command=self.add_task_dialog)
        add_button.grid(row=2, column=0, columnspan=3, pady=10, sticky="ew")
        
        # Rodapé
        footer = ttk.Label(self.root, 
                         text="by Ihago Albuquerque", 
                         style="Footer.TLabel",
                         anchor="center")
        footer.grid(row=3, column=0, columnspan=3, sticky="ew", padx=5, pady=5)
        
        # Configurar expansão
        self.root.rowconfigure(1, weight=1)

    def add_task_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Nova Tarefa")
        
        # Campos fixos
        ttk.Label(dialog, text="Título:").grid(row=0, column=0, padx=5, pady=2, sticky="e")
        title_entry = ttk.Entry(dialog, width=30)
        title_entry.grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(dialog, text="Descrição:").grid(row=1, column=0, padx=5, pady=2, sticky="e")
        desc_entry = ttk.Entry(dialog, width=30)
        desc_entry.grid(row=1, column=1, padx=5, pady=2)
        
        # Controle de recorrência
        ttk.Label(dialog, text="Recorrência:").grid(row=2, column=0, padx=5, pady=2, sticky="e")
        recurrence_var = tk.StringVar(value="Nenhuma")
        recurrence_combo = ttk.Combobox(dialog, textvariable=recurrence_var, 
                                      values=["Nenhuma", "Diária", "Semanal", "Mensal"], 
                                      state="readonly")
        recurrence_combo.grid(row=2, column=1, padx=5, pady=2)
        
        # Frame dinâmico para configurações
        config_frame = ttk.Frame(dialog)
        config_frame.grid(row=3, column=0, columnspan=2, sticky="ew", padx=5, pady=2)
        
        # Variáveis para configurações
        self.weekly_day = tk.StringVar()
        self.monthly_day = tk.IntVar()
        self.due_date_entry = tk.StringVar()
        
        def update_config():
            for widget in config_frame.winfo_children():
                widget.destroy()
            
            recurrence = recurrence_var.get()
            
            if recurrence == "Nenhuma":
                ttk.Label(config_frame, text="Data Término (dd/mm/aaaa):").grid(row=0, column=0, sticky="e")
                ttk.Entry(config_frame, textvariable=self.due_date_entry, width=20).grid(row=0, column=1, sticky="w")
            
            elif recurrence == "Diária":
                ttk.Label(config_frame, text="Tarefa diária - Data automática").grid(row=0, column=0, columnspan=2)
            
            elif recurrence == "Semanal":
                ttk.Label(config_frame, text="Dia da semana:").grid(row=0, column=0, sticky="e")
                ttk.Combobox(config_frame, textvariable=self.weekly_day, 
                           values=["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"], 
                           state="readonly", width=12).grid(row=0, column=1, sticky="w")
                self.weekly_day.set("Segunda")
            
            elif recurrence == "Mensal":
                ttk.Label(config_frame, text="Dia do mês:").grid(row=0, column=0, sticky="e")
                ttk.Spinbox(config_frame, textvariable=self.monthly_day, from_=1, to=31, width=5).grid(row=0, column=1, sticky="w")
                self.monthly_day.set(datetime.today().day)
        
        recurrence_var.trace_add("write", lambda *args: update_config())
        update_config()
        
        def submit():
            title = title_entry.get()
            description = desc_entry.get()
            recurrence = recurrence_var.get()
            due_date = ""
            recurrence_day = None
            
            if recurrence == "Nenhuma":
                due_date = self.due_date_entry.get()
                try:
                    datetime.strptime(due_date, "%d/%m/%Y")
                except ValueError:
                    messagebox.showerror("Erro", "Formato de data inválido! Use dd/mm/aaaa")
                    return
            
            elif recurrence == "Diária":
                due_date = datetime.today().strftime("%d/%m/%Y")
            
            elif recurrence == "Semanal":
                weekday_map = {
                    "Segunda": 0, "Terça": 1, "Quarta": 2,
                    "Quinta": 3, "Sexta": 4, "Sábado": 5, "Domingo": 6
                }
                target_day = weekday_map[self.weekly_day.get()]
                today = datetime.today()
                days_ahead = (target_day - today.weekday()) % 7
                if days_ahead == 0: days_ahead = 7
                due_date = (today + timedelta(days=days_ahead)).strftime("%d/%m/%Y")
                recurrence_day = self.weekly_day.get()
            
            elif recurrence == "Mensal":
                day = self.monthly_day.get()
                today = datetime.today()
                year = today.year
                month = today.month
                
                # Encontrar próxima data válida
                while True:
                    try:
                        next_date = datetime(year, month, day)
                        if next_date >= today:
                            break
                        else:
                            month += 1
                            if month > 12:
                                month = 1
                                year += 1
                    except ValueError:
                        month += 1
                        if month > 12:
                            month = 1
                            year += 1
                        last_day = (datetime(year, month, 1) - timedelta(days=1)).day
                        day = min(day, last_day)
                
                due_date = datetime(year, month, day).strftime("%d/%m/%Y")
                recurrence_day = day
            
            self.create_task(title, description, due_date, 0, recurrence, recurrence_day)
            dialog.destroy()
        
        ttk.Button(dialog, text="Criar", command=submit).grid(row=4, column=1, pady=5)

    def create_task(self, title, description, due_date, column_index, recurrence="Nenhuma", recurrence_day=None):
        container = self.column_frames[column_index]["container"]
        
        task_frame = ttk.Frame(container, relief="solid", padding=5)
        task_frame.pack(fill="x", pady=2)
        
        ttk.Label(task_frame, text=title, font=("Arial", 10, "bold")).pack(anchor="w")
        ttk.Label(task_frame, text=description).pack(anchor="w")
        ttk.Label(task_frame, text=f"Prazo: {due_date}", foreground="gray").pack(anchor="w")
        ttk.Label(task_frame, text=f"Recorrência: {recurrence}", foreground="blue").pack(anchor="w")
        
        controls = ttk.Frame(task_frame)
        controls.pack(fill="x", pady=5)
        
        ttk.Button(controls, text="←", width=3,
                 command=lambda: self.move_task(task_frame, -1)).pack(side="left")
        ttk.Button(controls, text="×", width=3,
                 command=lambda: self.delete_task(task_frame)).pack(side="left", padx=10)
        ttk.Button(controls, text="→", width=3,
                 command=lambda: self.move_task(task_frame, 1)).pack(side="left")
        
        self.columns[column_index]["tasks"].append({
            "frame": task_frame,
            "title": title,
            "description": description,
            "due_date": due_date,
            "recurrence": recurrence,
            "recurrence_day": recurrence_day
        })

    def move_task(self, task_frame, direction):
        current_col_idx, task_data = self.find_task(task_frame)
        if current_col_idx is None: return
        
        new_col_idx = current_col_idx + direction
        if 0 <= new_col_idx < len(self.columns):
            self.columns[current_col_idx]["tasks"].remove(task_data)
            task_data["frame"].destroy()
            
            self.create_task(
                task_data["title"],
                task_data["description"],
                task_data["due_date"],
                new_col_idx,
                task_data["recurrence"],
                task_data["recurrence_day"]
            )
            
            if new_col_idx == 2 and task_data["recurrence"] != "Nenhuma":
                self.create_recurring_task(task_data)

    def create_recurring_task(self, task_data):
        recurrence = task_data["recurrence"]
        today = datetime.today()
        
        if recurrence == "Diária":
            new_due = today + timedelta(days=1)
        elif recurrence == "Semanal":
            weekday_map = {
                "Segunda": 0, "Terça": 1, "Quarta": 2,
                "Quinta": 3, "Sexta": 4, "Sábado": 5, "Domingo": 6
            }
            target_day = weekday_map[task_data["recurrence_day"]]
            days_ahead = (target_day - today.weekday()) % 7
            if days_ahead == 0: days_ahead = 7
            new_due = today + timedelta(days=days_ahead)
        elif recurrence == "Mensal":
            day = task_data["recurrence_day"]
            month = today.month + 1
            year = today.year
            if month > 12:
                month = 1
                year += 1
            
            last_day = (datetime(year, month, 1) - timedelta(days=1)).day
            adjusted_day = min(day, last_day)
            new_due = datetime(year, month, adjusted_day)
        
        self.create_task(
            task_data["title"],
            task_data["description"],
            new_due.strftime("%d/%m/%Y"),
            0,
            recurrence,
            task_data["recurrence_day"]
        )

    def delete_task(self, task_frame):
        for column in self.columns:
            for task in column["tasks"]:
                if task["frame"] == task_frame:
                    column["tasks"].remove(task)
                    task["frame"].destroy()
                    return

    def find_task(self, task_frame):
        for i, column in enumerate(self.columns):
            for task in column["tasks"]:
                if task["frame"] == task_frame:
                    return i, task
        return None, None

    def load_tasks(self):
        try:
            with open(self.save_file, "r") as f:
                tasks = json.load(f)
                for task in tasks:
                    self.create_task(
                        title=task.get("title", "Sem título"),
                        description=task.get("description", ""),
                        due_date=task.get("due_date", "01/01/2000"),
                        column_index=task.get("column", 0),
                        recurrence=task.get("recurrence", "Nenhuma"),
                        recurrence_day=task.get("recurrence_day")
                    )
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def save_tasks(self):
        tasks_to_save = []
        for col_idx, column in enumerate(self.columns):
            for task in column["tasks"]:
                tasks_to_save.append({
                    "title": task["title"],
                    "description": task["description"],
                    "due_date": task["due_date"],
                    "column": col_idx,
                    "recurrence": task["recurrence"],
                    "recurrence_day": task["recurrence_day"]
                })
        with open(self.save_file, "w") as f:
            json.dump(tasks_to_save, f)

    def on_close(self):
        self.save_tasks()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()