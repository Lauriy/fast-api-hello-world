from sqlmodel import SQLModel, Field, create_engine, Session, Relationship


class TeamBase(SQLModel):
    name: str = Field(index=True)
    headquarters: str


class Team(TeamBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    heroes: list["Hero"] = Relationship(back_populates="team")


class TeamCreate(TeamBase):
    pass


class TeamPublic(TeamBase):
    id: int


class HeroBase(SQLModel):
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)
    team_id: int | None = Field(default=None, foreign_key="team.id")


class HeroPublic(HeroBase):
    id: int


class TeamPublicWithHeroes(TeamPublic):
    heroes: list[HeroPublic] = []


class TeamUpdate(SQLModel):
    name: str | None = None
    headquarters: str | None = None


class Hero(HeroBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str = Field()
    team: Team | None = Relationship(back_populates="heroes")


class HeroCreate(HeroBase):
    password: str


class HeroPublicWithTeam(HeroPublic):
    team: TeamPublic | None = None


class HeroUpdate(SQLModel):
    name: str | None = None
    secret_name: str | None = None
    age: int | None = None
    password: str | None = None
    team_id: int | None = None


def hash_password(password: str) -> str:
    # Use something like passlib here
    return f"not really hashed {password} hehehe"


DATABASE_URL = "postgresql://postgres:postgres@localhost/postgres"

# connect_args = {"check_same_thread": False}
engine = create_engine(DATABASE_URL, echo=True)
# connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
