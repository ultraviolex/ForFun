import tkinter as tk
import tkinter.font as tkfont
from random import sample

abdominalExercises = [
    'ab wheel',
    'russian twists',
    'crunches',
    'windshield wipers',
    'scissors',
    'plank',
    'v ups',
    'mountain climbers',
    'bicycles',
    'pulse ups',
    'hanging leg raises'
    ]

bicepsExercises = [
    'bicep curls w weights',
    'bicep curls w resistance band',
    'chin ups',
    'pull ups',
    'isometric pullup hold',
    'isometric chinup hold'
    ]

tricepsExercises = [
    'overhead tricep extensions',
    'skullcrushers',
    'diamond pushups',
    'tricep dips',
    'overhead pulldowns',
    'widegrip pull ups',
    'bent over dumbell rows'
    ]

chestExercises = [
    'pushups',
    'diamond pushups',
    'wide grip pushups',
    'one arm pushups',
    'clap pushups',
    'decline pushups',
    'incline pushups'
    ]


legExercises = [
    'squats',
    'sumo squats',
    'lunges',
    'romanian deadlifts',
    'standing calf raises',
    'jump squats',
    'side lunges',
    'single leg bridges'
]

backExercises = [
    'single arm dumbell rows',
    't raises',
    'delt raises',
    'push up hold',
    'deadlifts',
    'bent over band rows',
    'renegade rows',
    'bent over barbell rows'

]


class window:

    def __init__(self, main):

        self.frame = tk.Frame(main, bg='#CD6155')
        self.frame.pack(fill=tk.BOTH)

        vcmd = (main.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.titleFontStyle = tkfont.Font(size=20)
        self.title = tk.Label(
            self.frame, text="Workout Generator", font=self.titleFontStyle)
        self.title.configure(bg="#CD6155")
        self.title.pack(pady=15)

        self.muscle = tk.StringVar()
        self.muscle.set("abs")
        self.muscleLabel = tk.Label(
            self.frame, text="What are you working on today?")
        self.muscleLabel.configure(bg="#CD6155")
        self.musclesSelection = tk.OptionMenu(
            self.frame, self.muscle, "abs", "biceps", "triceps", "legs", "chest", "back")
        self.musclesSelection.configure(bg="#CD6155")
        self.muscleLabel.pack()
        self.musclesSelection.pack(pady=(0, 5))

        self.exercises = tk.StringVar()
        self.exercisesLabel = tk.Label(self.frame, text="How many exercises?")
        self.exercisesLabel.configure(bg="#CD6155")
        self.exercisesEntry = tk.Entry(self.frame, textvariable=self.exercises, bg="#AED6F1", highlightthickness=0,
                                       borderwidth=0, cursor="heart", validate='key', validatecommand=vcmd)
        self.exercisesLabel.pack()
        self.exercisesEntry.pack(pady=(0, 5))

        self.sets = tk.StringVar()
        self.setsLabel = tk.Label(self.frame, text="How many sets?")
        self.setsLabel.configure(bg="#CD6155")
        self.setsEntry = tk.Entry(self.frame, textvariable=self.sets,  bg='#AED6F1', highlightthickness=0, borderwidth=0,
                                  cursor='heart', validate='key', validatecommand=vcmd)
        self.setsLabel.pack()
        self.setsEntry.pack(pady=(0, 5))

        self.reps = tk.StringVar()
        self.repsLabel = tk.Label(self.frame, text="How many reps?")
        self.repsLabel.configure(bg="#CD6155")
        self.repsEntry = tk.Entry(self.frame, textvariable=self.reps, bg='#AED6F1', highlightthickness=0, borderwidth=0,
                                  cursor='heart', validate='key', validatecommand=vcmd)
        self.repsLabel.pack()
        self.repsEntry.pack(pady=(0, 5))

        self.getWorkoutButton = tk.Button(self.frame, text="Get workout", highlightbackground="#CD6155", cursor='heart',
                                          command=self.generate)
        self.getWorkoutButton.pack(pady=(10, 0))
        self.generated = tk.Label(self.frame, text="Coded by ultraviolex",  bg="#AED6F1",
                                  height=40, width=80, cursor='heart')
        self.generated.pack(pady=10, padx=10)

    def validate(self, action, index, value_if_allowed,
                 prior_value, text, validation_type, trigger_type, widget_name):

        if(action == '1'):
            if text in '0123456789.-+':
                try:
                    float(value_if_allowed)
                    return True
                except ValueError:
                    return False
            else:
                return False
        else:
            return True

    def generate(self):
        if (len(self.reps.get()) == 0 or len(self.sets.get()) == 0 or len(self.exercises.get()) == 0):
            self.generated['text'] = "pls fill in all fields <3"
        elif(self.reps.get() == "0" or self.sets.get() == "0" or self.exercises.get() == "0"):
            self.generated['text'] = "u cant have a field as zero >:/"
        elif (self.muscle.get() == 'abs'):
            self.workoutText = self.picker(abdominalExercises)
            self.generated['text'] = self.workoutText
        elif (self.muscle.get() == 'biceps'):
            self.workoutText = self.picker(bicepsExercises)
            self.generated['text'] = self.workoutText
        elif (self.muscle.get() == 'triceps'):
            self.workoutText = self.picker(tricepsExercises)
            self.generated['text'] = self.workoutText
        elif (self.muscle.get() == 'legs'):
            self.workoutText = self.picker(legExercises)
            self.generated['text'] = self.workoutText
        elif (self.muscle.get() == 'chest'):
            self.workoutText = self.picker(chestExercises)
            self.generated['text'] = self.workoutText
        elif (self.muscle.get() == 'back'):
            self.workoutText = self.picker(backExercises)
            self.generated['text'] = self.workoutText
        else:
            self.generated['text'] = 'somehow u broke it :( \nsend a screenshot to violex'

    def picker(self, exerciseList):
        self.final = ""
        try:
            self.picked = sample(exerciseList, int(self.exercises.get()))
        except:
            return "theres not enough exercises in the list :( \npls put in a number less than " + str((1+len(exerciseList)))
            + " in the exercises field :)"
        for e in self.picked:
            if (e == 'plank' or e == 'mountain climbers' or "hold" in e):
                self.final = self.final + e + ": till exhaustion\n"
            else:
                self.final = self.final + e + ": " + self.sets.get() + "x" + \
                    self.reps.get() + "\n"
        return self.final


root = tk.Tk(className="Workout Generator")
root.configure(bg='#CD6155')
root.geometry("400x600")
window(root)
root.mainloop()
