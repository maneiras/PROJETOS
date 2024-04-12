import customtkinter as ctk
from tkinter import *
from openpyxl import Workbook

class App(ctk.CTk):  
    def __init__(self):
        super().__init__()
        self.layout_config()  
        self.appearence()
        self.todo_sistema()
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(["Nome", "Contato", "Idade", "Gênero", "Observações"])

    def layout_config(self):
        self.title("Sistema de Gestao De Clientes")
        self.geometry("700x500")

    def appearence(self): 
        self.lb_apm = ctk.CTkLabel(self, text="Tema:", bg_color="transparent", text_color='#000')
        self.lb_apm.place(x=50, y=430)
        
        self.opt_apm = ctk.CTkOptionMenu(self, values=["light", "Dark", "System"], command=self.change_apm)
        self.opt_apm.place(x=50, y=460)

    def todo_sistema(self):  
        frame = ctk.CTkFrame(self, width=700, height=50, corner_radius=0, bg_color="teal", fg_color="teal")
        frame.place(x=0, y=10)
        
        title = ctk.CTkLabel(frame, text="Sistema de Gestao de Clientes", font=("century Gothic bold", 24), text_color="#fff")
        title.place(x=10, y=10)

        span = ctk.CTkLabel(self, text="Por favor, Preencha todos os campos", font=("century Gothic bold", 24), text_color=["#000","#fff"])
        span.place(x=50, y=70)

        # Text variables
        self.name_value = StringVar()
        self.contact_value = StringVar()
        self.age_value = StringVar()
        self.address_value = StringVar()

        # Entries
        self.name_entry = ctk.CTkEntry(self, width=150, textvariable=self.name_value, font=("century,Gothic",16), fg_color="transparent")
        self.name_entry.place(x=50, y=150)

        self.contact_entry = ctk.CTkEntry(self, width=150, textvariable=self.contact_value, font=("century,Gothic",16), fg_color="transparent")
        self.contact_entry.place(x=450, y=150)

        self.age_entry = ctk.CTkEntry(self, width=150, textvariable=self.age_value, font=("century,Gothic",16), fg_color="transparent")
        self.age_entry.place(x=300, y=220)

        self.address_entry = ctk.CTkEntry(self, width=150, textvariable=self.address_value, font=("century,Gothic",16), fg_color="transparent")
        self.address_entry.place(x=50, y=220)

        # ComboBox
        self.gender_combobox = ctk.CTkComboBox(self, values=["Masculino","Feminino"], font=("century Gothic bold",14))
        self.gender_combobox.place(x=500, y=220)
        self.gender_combobox.set("Masculino")

        # Textbox
        self.obs_entry = ctk.CTkTextbox(self, width=50, height=10, font=("Century Gothic", 14), fg_color="transparent")
        self.obs_entry.place(x=200, y=250)

        # Buttons
        btn_submit = ctk.CTkButton(self, text="Salvar Dados", command=self.salvar_dados, fg_color="#151")
        btn_submit.place(x=200, y=400)

        btn_clear = ctk.CTkButton(self, text="Limpar Dados", command=self.limpar_dados, fg_color="#555")
        btn_clear.place(x=350, y=400)

        # Labels
        lb_name = ctk.CTkLabel(self, text="Nome:", font=("century Gothic bold", 24), text_color=["#000","#fff"])
        lb_name.place(x=50, y=120)

        lb_contact = ctk.CTkLabel(self, text="Contato:", font=("century Gothic bold", 24), text_color=["#000","#fff"])
        lb_contact.place(x=450, y=120)

        lb_age = ctk.CTkLabel(self, text="Idade:", font=("century Gothic bold", 24), text_color=["#000","#fff"])
        lb_age.place(x=300, y=190)

        lb_gender = ctk.CTkLabel(self, text="Gênero:", font=("century Gothic bold", 24), text_color=["#000","#fff"])
        lb_gender.place(x=500, y=190)

        lb_adress = ctk.CTkLabel(self, text="Endereço:", font=("century Gothic bold", 24), text_color=["#000","#fff"])
        lb_adress.place(x=50, y=190)

        lb_observations = ctk.CTkLabel(self, text="Observações:", font=("century Gothic bold", 24), text_color=["#000","#fff"])
        lb_observations.place(x=50, y=250)
      
    def change_apm(self, nova_aparencia):
        ctk.set_appearance_mode(nova_aparencia) # Mudar a cor

    def salvar_dados(self):
        name = self.name_value.get()
        contato = self.contact_value.get()
        age = self.age_value.get()
        gender = self.gender_combobox.get()
        obs = self.obs_entry.get("1.0", END)
        
        # Adicionar dados à planilha
        self.ws.append([name, contato, age, gender, obs])
        
        # Salvar planilha
        self.wb.save("dados_clientes.xlsx")
        
        print("Dados salvos com sucesso!")

    def limpar_dados(self):
        self.name_value.set("")
        self.contact_value.set("")
        self.age_value.set("")
        self.address_value.set("")
        self.gender_combobox.set("Masculino")
        self.obs_entry.delete("1.0", END)

if __name__ == "__main__":
    my_app = App()
    my_app.mainloop()