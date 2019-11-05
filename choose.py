import abc
import random


class BaseChooser(metaclass=abc.ABCMeta):
    participants = None

    @abc.abstractmethod
    def finalize_list(self):
        pass

    def set_participants(self, participants_dict):
        self.participants = participants_dict


class BasicChooser(BaseChooser):
    def _randomize(self):
        result = list(self.participants.keys())
        random.shuffle(result)
        return result

    def finalize_list(self):
        lst = self._randomize()
        result_dict = {}
        for i, person in enumerate(lst[:-1]):
            result_dict[person] = self.participants[person]
            result_dict[person]["friend"] = lst[i + 1]
        result_dict[lst[-1]] = self.participants[lst[-1]]
        result_dict[lst[-1]]["friend"] = lst[0]
        return result_dict


class PseudoBlackListChooser(BasicChooser):
    def finalize_list(self):
        count = 10 ** 10
        i = 0
        result = None
        while i < count and not result:
            result = super().finalize_list()
            for res in result.values():
                if res['friend'] in res['blacklist']:
                    result = None
                    break
            i += 1
        if not result:
            raise Exception('Impossible')
        return result


class BlackListChooser(BaseChooser):

    def recursive_sort(self, current_participant, participants, first_step=False):
        if len(participants) == 0:
            return [current_participant]
        participants_for_current = [el for el in participants if
                                    el not in self.participants[current_participant]['blacklist']]
        random.shuffle(participants_for_current)
        # print(current_participant)
        # print(participants_for_current)
        # print(participants)
        result_list = [current_participant]
        inserted = False
        for i, next_participant in enumerate(participants_for_current):
            next_participant_index = participants.index(next_participant)
            result = self.recursive_sort(next_participant,
                                         participants[:next_participant_index] + participants[
                                                                                 next_participant_index + 1:])
            if result and not first_step:
                result_list += result
                inserted = True
                break
            elif result and first_step:
                if result[-1] not in self.participants[current_participant]['blacklist']:
                    result_list += result
                    inserted = True
                    break
        if inserted:
            return result_list
        return None

    def finalize_list(self):
        lst = list(self.participants.keys())
        random.shuffle(lst)
        result = self.recursive_sort(lst[0], lst[1:], True)
        print(result)
        if not result:
            raise Exception('Impossible')
        result_dict = {}
        for i, person in enumerate(lst[:-1]):
            result_dict[person] = self.participants[person]
            result_dict[person]["friend"] = lst[i + 1]
        result_dict[lst[-1]] = self.participants[lst[-1]]
        result_dict[lst[-1]]["friend"] = lst[0]
        return result_dict
