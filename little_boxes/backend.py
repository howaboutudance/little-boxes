import abc
import typing

if typing.TYPE_CHECKING:
    from little_boxes import activitypub as ap


class Backend(abc.ABC):
    @abc.abstractmethod
    def fetch_iri(self, iri: str) -> "ap.ObjectType":
        pass

    @abc.abstractmethod
    def activity_url(self, obj_id: str) -> str:
        pass

    @abc.abstractmethod
    def outbox_create(self, as_actor: "ap.Person", activity: "ap.Create") -> None:
        pass

    @abc.abstractmethod
    def inbox_create(self, as_actor: "ap.Person", activity: "ap.Create") -> None:
        pass

    @abc.abstractmethod
    def outbox_is_blocked(self, as_actor: "ap.Person", actor_id: str) -> bool:
        pass

    @abc.abstractmethod
    def inbox_new(self, as_actor: "ap.Person", activity: "ap.BaseActivity") -> None:
        pass

    @abc.abstractmethod
    def outbox_new(self, as_actor: "ap.Person", activity: "ap.BaseActivity") -> None:
        pass

    @abc.abstractmethod
    def new_follower(self, as_actor: "ap.Person", follow: "ap.Follow") -> None:
        pass

    @abc.abstractmethod
    def new_following(self, as_actor: "ap.Person", follow: "ap.Follow") -> None:
        pass

    @abc.abstractmethod
    def undo_new_follower(self, as_actor: "ap.Person", follow: "ap.Follow") -> None:
        pass

    @abc.abstractmethod
    def undo_new_following(self, as_actor: "ap.Person", follow: "ap.Follow") -> None:
        pass

    @abc.abstractmethod
    def inbox_update(self, as_actor: "ap.Person", activity: "ap.Update") -> None:
        pass
