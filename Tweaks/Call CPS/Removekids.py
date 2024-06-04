import sims4.commands
import services
from sims.sim_info_lod import SimInfoLODLevel
from interactions.utils.death import DeathTracker
from objects import ALL_HIDDEN_REASONS

@sims4.commands.Command('danitysimmer.vanish_sim', command_type=sims4.commands.CommandType.Live)
def vanish_sim(sim_, _connection=None):
    try:
        if not sim_:
            return

        sim_info_manager = services.sim_info_manager()
        sim_info = sim_info_manager.get(int(sim_))

        sim_info.household.remove_sim_info(sim_info, destroy_if_empty_household=True)
        client = services.client_manager().get_first_client()

        client.remove_selectable_sim_info(sim_info)
        sim_info.transfer_to_hidden_household()
        sim_info.request_lod(SimInfoLODLevel.MINIMUM)
        sim_info.inject_into_inactive_zone(DeathTracker.DEATH_ZONE_ID, start_away_actions=False,
                                           skip_instanced_check=True, skip_daycare=True)
        sim = sim_info.get_sim_instance(allow_hidden_flags=ALL_HIDDEN_REASONS)
        if sim:
            sim.schedule_destroy_asap(post_delete_func=None, source=sim, cause='Sim died.')
    except Exception as e:
        raise Exception(f"Error with Vanish Sim: {str(e)}")
