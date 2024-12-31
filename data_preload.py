from database import db_session
from models import Topic, Passage, Question

data = {
    "Nature": {
        "passage": "The water cycle describes the continuous movement of water on, above, and below the surface of the Earth. This process is driven primarily by the Sun's energy and involves evaporation, condensation, precipitation, and collection. Water evaporates from oceans, rivers, and lakes into the atmosphere, condenses to form clouds, and eventually falls back to the surface as precipitation. It supports ecosystems, regulates temperature, and shapes the Earth's surface.",
        "questions": [
            {"question": "What drives the water cycle?", "options": ["The Moon", "The Sun", "Gravity", "Earth's Core"], "answer": "The Sun"},
            {"question": "What process turns water into vapor?", "options": ["Condensation", "Evaporation", "Precipitation", "Transpiration"], "answer": "Evaporation"},
            {"question": "What forms clouds?", "options": ["Condensed water vapor", "Frozen rivers", "Evaporated soil", "Melting snow"], "answer": "Condensed water vapor"},
            {"question": "Which stage returns water to the ground?", "options": ["Evaporation", "Condensation", "Precipitation", "Sublimation"], "answer": "Precipitation"},
            {"question": "What is another term for collection?", "options": ["Accumulation", "Evaporation", "Infiltration", "Transpiration"], "answer": "Accumulation"},
            {"question": "Where does most evaporation occur?", "options": ["Forests", "Oceans", "Mountains", "Glaciers"], "answer": "Oceans"},
            {"question": "Which process involves plant water release?", "options": ["Precipitation", "Transpiration", "Evaporation", "Condensation"], "answer": "Transpiration"},
            {"question": "What happens during condensation?", "options": ["Water vapor cools", "Water turns to vapor", "Water absorbs heat", "Snow melts"], "answer": "Water vapor cools"},
            {"question": "What state is water in clouds?", "options": ["Liquid or solid", "Vapor only", "Gas and plasma", "Ice only"], "answer": "Liquid or solid"},
            {"question": "What regulates Earth's temperature?", "options": ["The water cycle", "Volcanoes", "Moon phases", "Magnetic poles"], "answer": "The water cycle"},
        ]
    },
    "Science": {
        "passage": "Atoms are the fundamental building blocks of matter. Each atom consists of a nucleus, made of protons and neutrons, surrounded by electrons orbiting in shells. The number of protons determines an element's identity, while the arrangement of electrons defines its chemical behavior. Atoms combine to form molecules through chemical bonds. Advances in atomic theory have led to innovations in technology, medicine, and energy, making understanding atomic structure essential in modern science.",
        "questions": [
            {"question": "What is the basic unit of matter?", "options": ["Molecules", "Atoms", "Cells", "Compounds"], "answer": "Atoms"},
            {"question": "What particles are in an atom's nucleus?", "options": ["Electrons", "Protons and neutrons", "Ions", "Molecules"], "answer": "Protons and neutrons"},
            {"question": "What defines an element's identity?", "options": ["Number of protons", "Number of neutrons", "Electron arrangement", "Atomic size"], "answer": "Number of protons"},
            {"question": "What surrounds the nucleus?", "options": ["Electrons", "Protons", "Neutrons", "Ions"], "answer": "Electrons"},
            {"question": "How do atoms form molecules?", "options": ["Through chemical bonds", "Through reactions", "Through fission", "Through fusion"], "answer": "Through chemical bonds"},
            {"question": "What is an electron's charge?", "options": ["Positive", "Neutral", "Negative", "Variable"], "answer": "Negative"},
            {"question": "What particle has no charge?", "options": ["Proton", "Neutron", "Electron", "Atom"], "answer": "Neutron"},
            {"question": "What type of bond shares electrons?", "options": ["Covalent", "Ionic", "Hydrogen", "Metallic"], "answer": "Covalent"},
            {"question": "What does atomic theory study?", "options": ["Molecules", "Atoms", "Cells", "Nucleons"], "answer": "Atoms"},
            {"question": "What determines chemical behavior?", "options": ["Electron arrangement", "Proton number", "Neutron number", "Mass"], "answer": "Electron arrangement"},
        ]
    },
    "History": {
        "passage": "The Industrial Revolution marked a pivotal period in history, beginning in the 18th century in Britain. This era saw the transition from hand production to machines, with innovations like the steam engine and mechanized textile production. Urbanization grew as people moved to cities for factory jobs, leading to social, economic, and technological changes. The revolution reshaped industries, transportation, and living conditions, laying the groundwork for modern economies.",
        "questions": [
            {"question": "Where did the Industrial Revolution begin?", "options": ["France", "Britain", "Germany", "USA"], "answer": "Britain"},
            {"question": "What powered early factories?", "options": ["Steam engines", "Electric motors", "Wind turbines", "Solar panels"], "answer": "Steam engines"},
            {"question": "What industry was first mechanized?", "options": ["Textile", "Agriculture", "Mining", "Transportation"], "answer": "Textile"},
            {"question": "What caused urbanization?", "options": ["Factory jobs", "Railroads", "Steamships", "Agriculture"], "answer": "Factory jobs"},
            {"question": "What replaced hand production?", "options": ["Machines", "Factories", "Electricity", "Robots"], "answer": "Machines"},
            {"question": "What period did this revolution occur?", "options": ["18th century", "19th century", "20th century", "17th century"], "answer": "18th century"},
            {"question": "What is urbanization?", "options": ["Moving to cities", "Building factories", "Growing crops", "Learning new skills"], "answer": "Moving to cities"},
            {"question": "Which invention revolutionized transport?", "options": ["Steam engine", "Cotton gin", "Spinning jenny", "Printing press"], "answer": "Steam engine"},
            {"question": "What was a social change?", "options": ["Class mobility", "Nobility rise", "Fewer cities", "Farming growth"], "answer": "Class mobility"},
            {"question": "What laid the foundation for economies?", "options": ["Industrial Revolution", "World Wars", "Colonial trade", "Agriculture"], "answer": "Industrial Revolution"},
        ]
    },
    "Literature": {
        "passage": "William Shakespeare is one of the most celebrated playwrights and poets in history. Born in 1564 in England, his works explore timeless themes like love, power, betrayal, and ambition. Famous plays like 'Hamlet,' 'Macbeth,' and 'Romeo and Juliet' showcase his mastery of language and storytelling. His influence extends beyond literature, inspiring countless adaptations and interpretations in art, theater, and film, making him a cultural icon of the English-speaking world.",
        "questions": [
            {"question": "When was Shakespeare born?", "options": ["1564", "1600", "1700", "1800"], "answer": "1564"},
            {"question": "What is Shakespeare famous for?", "options": ["Plays and poetry", "Science", "Philosophy", "Politics"], "answer": "Plays and poetry"},
            {"question": "Which is NOT a Shakespeare play?", "options": ["Macbeth", "Hamlet", "Pride and Prejudice", "Romeo and Juliet"], "answer": "Pride and Prejudice"},
            {"question": "What themes did he explore?", "options": ["Love and power", "Space and time", "Nature and science", "Trade and economy"], "answer": "Love and power"},
            {"question": "What is 'Romeo and Juliet' about?", "options": ["Star-crossed lovers", "War and peace", "Political betrayal", "Family wealth"], "answer": "Star-crossed lovers"},
            {"question": "Where was Shakespeare born?", "options": ["England", "France", "Italy", "Germany"], "answer": "England"},
            {"question": "What did he influence?", "options": ["Art and theater", "Biology", "Economics", "Physics"], "answer": "Art and theater"},
            {"question": "Which play features Macbeth?", "options": ["Macbeth", "Hamlet", "Othello", "King Lear"], "answer": "Macbeth"},
            {"question": "What era was he part of?", "options": ["Elizabethan", "Victorian", "Medieval", "Modern"], "answer": "Elizabethan"},
            {"question": "What is Shakespeare's legacy?", "options": ["Cultural icon", "Military leader", "Economic theorist", "Scientific pioneer"], "answer": "Cultural icon"},
        ]
    }
}


def preload_data():
    try:
        for topic_name, topic_data in data.items():

            topic = Topic(name=topic_name)
            db_session.add(topic)
            db_session.commit()


            passage = Passage(text=topic_data["passage"], topic_id=topic.id)
            db_session.add(passage)
            db_session.commit()


            for q in topic_data["questions"]:
                question = Question(
                    question=q["question"],
                    options=",".join(q["options"]),
                    correct_option=q["answer"],
                    passage_id=passage.id
                )
                db_session.add(question)

            db_session.commit()
    except Exception as e:
        db_session.rollback()
        print(f"Error: {e}")
    finally:
        db_session.close()


if __name__ == "__main__":
    preload_data()
