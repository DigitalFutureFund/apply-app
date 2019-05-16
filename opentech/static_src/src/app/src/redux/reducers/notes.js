import { combineReducers } from 'redux';

import {
    UPDATE_NOTE,
    UPDATE_NOTES,
    START_FETCHING_NOTES,
    FAIL_FETCHING_NOTES,
    START_CREATING_NOTE_FOR_SUBMISSION,
    FAIL_CREATING_NOTE_FOR_SUBMISSION,
    UPDATE_EDIT_NOTE,
} from '@actions/notes';

function notesFetching(state = false, action) {
    switch (action.type) {
        case START_FETCHING_NOTES:
            return true;
        case UPDATE_NOTES:
        case FAIL_FETCHING_NOTES:
            return false;
        default:
            return state;
    }
}

function notesErrored(state = {errored: false, message: null}, action) {
    switch (action.type) {
        case UPDATE_NOTES:
        case START_FETCHING_NOTES:
        return {
            ...state,
            errored: false,
        };
        case FAIL_FETCHING_NOTES:
            return {
                ...state,
                message: action.error,
                errored: true,
            };
        default:
            return state;
    }
}

function note(state, action) {
    switch (action.type) {
        case UPDATE_NOTE:
            return {
                ...state,
                ...action.data,
            };
        default:
            return state;
    }
}

function notesCreating(state = [], action) {
    switch (action.type) {
        case START_CREATING_NOTE_FOR_SUBMISSION:
            return [
                ...state,
                action.submissionID,
            ];
        case UPDATE_NOTE:
        case FAIL_CREATING_NOTE_FOR_SUBMISSION:
            return state.filter(v => v !== action.submissionID);
        default:
            return state
    }
}


function notesFailedCreating(state = {}, action) {
    switch (action.type) {
        case UPDATE_NOTE:
        case START_CREATING_NOTE_FOR_SUBMISSION:
            return Object.entries(state).reduce((acc, [k, v]) => {
                if (parseInt(k) !== action.submissionID) {
                    acc[k] = v;
                }
                return acc;
            }, {});
        case FAIL_CREATING_NOTE_FOR_SUBMISSION:
            return {
                ...state,
                [action.submissionID]: action.error,
            };
        default:
            return state
    }
}

function notesByID(state = {}, action) {
    switch (action.type) {
        case UPDATE_NOTES:
            return {
                ...state,
                ...action.data.results.reduce((newNotesAccumulator, newNote) => {
                    newNotesAccumulator[newNote.id] = note(state[newNote.id], {
                        type: UPDATE_NOTE,
                        data: newNote,
                    });
                    return newNotesAccumulator;
                }, {}),
            };
        case UPDATE_NOTE:
            return {
                ...state,
                [action.data.id]: note(state[action.data.id], {
                    type: UPDATE_NOTE,
                    data: action.data,
                }),
            };
        default:
            return state;
    }
}

function editingNote(state={}, action) {
    switch (action.type) {
        case UPDATE_EDIT_NOTE:
            return {
                ...state,
                [action.submissionID] : {
                    id: action.messageID,
                    message: action.message,
                },
            };
        default:
            return state;
    }
}

export default combineReducers({
    byID: notesByID,
    isFetching: notesFetching,
    error: notesErrored,
    createError: notesFailedCreating,
    isCreating: notesCreating,
    editing: editingNote,
});
